def search_by_id(employees, employee_id):

    for employee in employees:

        if employee.employee_id == employee_id:
            return employee

    return None


def search_by_name(employees, name):

    for employee in employees:

        if employee.name.lower() == name.lower():
            return employee

    return None