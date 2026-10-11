import json


def save_employees_json(employees, filename):

    if not employees:
        print("No employees to save.")
        return

    employee_data = []

    for employee in employees:
        employee_data.append(employee.to_dict())

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            employee_data,
            file,
            indent=4
        )

    print(
        f"Employee data saved to {filename}"
    )