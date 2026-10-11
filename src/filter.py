def filter_by_department(employees, department):

    filtered_employees = []

    for employee in employees:

        if employee.department.lower() == department.lower():

            filtered_employees.append(employee)

    return filtered_employees