def validate_required_fields(employee):

    required_fields = [
        "employee_id",
        "name",
        "department",
        "salary",
        "email"
    ]

    missing_fields = []

    for field in required_fields:

        if not employee.get(field):
            missing_fields.append(field)

    return missing_fields


def validate_employee_id(employee_id):

    try:

        employee_id = int(employee_id)

        if employee_id <= 0:
            return False

        return True

    except ValueError:

        return False


def validate_salary(salary):

    try:

        salary = int(salary)

        if salary <= 0:
            return False

        return True

    except ValueError:

        return False


def validate_name(name):

    if not name:
        return False

    if not name.strip():
        return False

    return True


def validate_department(department):

    if not department:
        return False

    if not department.strip():
        return False

    return True


def validate_email(email):

    if not email:
        return False

    email = email.strip()

    if "@" not in email:
        return False

    if "." not in email:
        return False

    return True