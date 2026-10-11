
import csv
import json


def clean_employee(employee):
    cleaned_employee = {}

    for field, value in employee.items():
        if not isinstance(field, str):
            raise ValueError(
                "Employee field names must be strings."
            )

        cleaned_field = field.strip().lower()

        if isinstance(value, str):
            cleaned_employee[cleaned_field] = value.strip()
        else:
            cleaned_employee[cleaned_field] = value

    return cleaned_employee


def validate_csv_headers(headers):
    required_fields = [
        "employee_id",
        "name",
        "department",
        "salary",
        "email"
    ]

    missing_fields = []

    for field in required_fields:
        if field not in headers:
            missing_fields.append(field)

    if missing_fields:
        raise ValueError(
            f"CSV is missing required columns: {missing_fields}"
        )


def load_csv(filename):
    employees = []

    with open(filename, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            raise ValueError("CSV file has no headers.")

        reader.fieldnames = [
            field.strip().lower()
            for field in reader.fieldnames
        ]

        validate_csv_headers(reader.fieldnames)

        for row in reader:
            cleaned_row = clean_employee(row)
            employees.append(cleaned_row)

    if not employees:
        raise ValueError(
            "CSV file contains no employee records."
        )

    return employees


def load_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        employees = json.load(file)

    if not isinstance(employees, list):
        raise ValueError(
            "JSON data must contain a list of employees."
        )

    if not employees:
        raise ValueError(
            "JSON file contains no employee records."
        )

    cleaned_employees = []

    for employee in employees:
        if not isinstance(employee, dict):
            raise ValueError(
                "Each employee record must be a dictionary."
            )

        cleaned_employee = clean_employee(employee)
        cleaned_employees.append(cleaned_employee)

    return cleaned_employees


def load_employees(filename):
    try:
        if filename.lower().endswith(".csv"):
            return load_csv(filename)

        elif filename.lower().endswith(".json"):
            return load_json(filename)

        else:
            raise ValueError(
                "Unsupported file format. Use CSV or JSON."
            )

    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None

    except json.JSONDecodeError:
        print(f"Invalid JSON format: {filename}")
        return None

    except PermissionError:
        print(f"Permission denied: {filename}")
        return None

    except ValueError as error:
        print(f"Invalid file data: {error}")
        return None

    except Exception as error:
        print(
            f"Unexpected error while loading file: {error}"
        )
        return None