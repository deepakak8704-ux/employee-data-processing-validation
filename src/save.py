import csv


def save_valid_employees(employees, filename):

    if not employees:

        print(
            "No valid employees to save."
        )

        return

    fieldnames = [
        "employee_id",
        "name",
        "department",
        "salary",
        "email"
    ]

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for employee in employees:

            writer.writerow(
                employee.to_dict()
            )

    print(
        f"\nValidated employee data "
        f"saved to {filename}"
    )