from validator import (
    validate_required_fields,
    validate_employee_id,
    validate_salary,
    validate_name,
    validate_department,
    validate_email
)

from report import (
    generate_quality_report,
    save_quality_report
)

from search import (
    search_by_id,
    search_by_name
)

from filter import (
    filter_by_department
)

from statistics import (
    get_employee_count,
    get_department_counts,
    get_average_salary,
    get_highest_salary
)

from save import (
    save_valid_employees
)

from loader import (
    load_employees
)

from logger import logger
from json_save import save_employees_json
from employee import (
    create_employee_objects
)


def show_menu():

    print("\nEmployee Data Processing System")
    print("--------------------------------")
    print("1. Search Employee")
    print("2. Filter by Department")
    print("3. Show Statistics")
    print("4. Exit")


def search_employee(employees):

    print("\nSearch Employee")
    print("----------------")
    print("1. Search by ID")
    print("2. Search by Name")

    choice = input(
        "\nEnter your choice: "
    ).strip()

    if choice == "1":

        try:

            employee_id = int(
                input("Enter employee ID: ")
            )

            result = search_by_id(
                employees,
                employee_id
            )

            if result:

                result.display_info()

            else:

                print("\nEmployee not found.")

        except ValueError:

            print(
                "\nInvalid employee ID."
            )

    elif choice == "2":

        name = input(
            "Enter employee name: "
        ).strip()

        result = search_by_name(
            employees,
            name
        )

        if result:

            result.display_info()

        else:

            print("\nEmployee not found.")

    else:

        print("\nInvalid choice.")


def filter_employees(employees):

    department = input(
        "\nEnter department: "
    ).strip()

    filtered_employees = filter_by_department(
        employees,
        department
    )

    if filtered_employees:

        print(
            f"\nEmployees in {department}:"
        )

        for employee in filtered_employees:

            employee.display_info()

    else:

        print(
            "\nNo employees found "
            "in that department."
        )


def show_statistics(employees):

    print("\nEmployee Statistics")
    print("--------------------")

    employee_count = get_employee_count(
        employees
    )

    department_counts = get_department_counts(
        employees
    )

    average_salary = get_average_salary(
        employees
    )

    highest_salary = get_highest_salary(
        employees
    )

    print(
        f"Employee Count: "
        f"{employee_count}"
    )

    print("\nDepartment-wise Count:")

    for department, count in department_counts.items():

        print(
            f"{department}: {count}"
        )

    print(
        f"\nAverage Salary: "
        f"{average_salary}"
    )

    print(
        f"Highest Salary: "
        f"{highest_salary}"
    )


def select_input_file():

    while True:

        print("\nSelect Input File")
        print("-----------------")
        print("1. CSV")
        print("2. JSON")

        choice = input(
            "\nEnter your choice: "
        ).strip()

        if choice == "1":

            return "data/employees.csv"

        elif choice == "2":

            return "data/employees.json"

        else:

            print(
                "\nInvalid choice. "
                "Please select 1 or 2."
            )


def main():

    print(
        "\nEmployee Data Processing "
        "and Validation System"
    )

    # Select input file

    input_file = select_input_file()

    logger.info(
        f"Selected input file: {input_file}"
    )

    # Load employee data

    raw_employees = load_employees(
        input_file
    )

    if raw_employees is None:

        logger.error(
            f"Failed to load employee data "
            f"from {input_file}"
        )

        return

    logger.info(
        f"Loaded {len(raw_employees)} "
        f"employee records"
    )

    # Validation

    employees = []

    employee_ids = set()

    validation_errors = []

    for employee in raw_employees:

        employee_errors = []

        missing_fields = (
            validate_required_fields(
                employee
            )
        )

        if missing_fields:

            employee_errors.append(
                f"Missing fields: "
                f"{missing_fields}"
            )

        # Validate Employee ID

        if "employee_id" not in missing_fields:

            if not validate_employee_id(
                employee["employee_id"]
            ):

                employee_errors.append(
                    "Invalid employee ID"
                )

            else:

                employee["employee_id"] = int(
                    employee["employee_id"]
                )

                if (
                    employee["employee_id"]
                    in employee_ids
                ):

                    employee_errors.append(
                        "Duplicate employee ID"
                    )

                else:

                    employee_ids.add(
                        employee["employee_id"]
                    )

        # Validate Name

        if "name" not in missing_fields:

            if not validate_name(
                employee["name"]
            ):

                employee_errors.append(
                    "Invalid name"
                )

        # Validate Department

        if "department" not in missing_fields:

            if not validate_department(
                employee["department"]
            ):

                employee_errors.append(
                    "Invalid department"
                )

        # Validate Salary

        if "salary" not in missing_fields:

            if not validate_salary(
                employee["salary"]
            ):

                employee_errors.append(
                    "Invalid salary"
                )

            else:

                employee["salary"] = int(
                    employee["salary"]
                )

        # Validate Email

        if "email" not in missing_fields:

            if not validate_email(
                employee["email"]
            ):

                employee_errors.append(
                    "Invalid email"
                )

        # Store validation result

        if employee_errors:

            validation_errors.append(
                {
                    "employee_id": employee.get(
                        "employee_id"
                    ),
                    "errors": employee_errors
                }
            )

            logger.warning(
                f"Validation errors for "
                f"employee "
                f"{employee.get('employee_id')}: "
                f"{employee_errors}"
            )

        else:

            employees.append(employee)

    # Display validation summary

    print(
        f"\nValid employees: "
        f"{len(employees)}"
    )

    print(
        f"Invalid employees: "
        f"{len(validation_errors)}"
    )

    # Generate quality report

    report = generate_quality_report(
        employees,
        validation_errors
    )

    print("\nData Quality Report")
    print("--------------------")

    print(
        f"Total Records: "
        f"{report['total_records']}"
    )

    print(
        f"Valid Records: "
        f"{report['valid_records']}"
    )

    print(
        f"Invalid Records: "
        f"{report['invalid_records']}"
    )

    print(
        f"Total Errors: "
        f"{report['total_errors']}"
    )

    print("\nError Summary")

    for error, count in report[
        "error_counts"
    ].items():

        print(
            f"{error}: {count}"
        )

    # Convert valid dictionaries
    # into Employee objects

    employee_objects = create_employee_objects(
        employees
    )

    print(
        "\nEmployee objects created: "
        f"{len(employee_objects)}"
    )

    logger.info(
        f"Created {len(employee_objects)} "
        f"Employee objects"
    )

    # Save validated employee data

    save_valid_employees(
        employee_objects,
        "output/validated_employees.csv"
    )

    logger.info(
        "Validated employee data saved."
    )

    save_employees_json(
        employee_objects,
        "output/validated_employees.json"
    )
    logger.info("Validated employee JSON data saved.")

    # Save quality report

    save_quality_report(
        report,
        "output/data_quality_report.txt"
    )

    logger.info(
        "Data quality report saved."
    )

    # Main menu

    while True:

        show_menu()

        choice = input(
            "\nEnter your choice: "
        ).strip()

        if choice == "1":

            search_employee(
                employee_objects
            )

        elif choice == "2":

            filter_employees(
                employee_objects
            )

        elif choice == "3":

            show_statistics(
                employee_objects
            )

        elif choice == "4":

            print(
                "\nExiting program..."
            )

            logger.info(
                "Application completed."
            )

            break

        else:

            print(
                "\nInvalid choice. "
                "Please select 1-4."
            )


if __name__ == "__main__":

    main()