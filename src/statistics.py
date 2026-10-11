def get_employee_count(employees):

    return len(employees)


def get_department_counts(employees):

    department_counts = {}

    for employee in employees:

        department = employee.department

        if department in department_counts:

            department_counts[department] += 1

        else:

            department_counts[department] = 1

    return department_counts


def get_average_salary(employees):

    if not employees:
        return 0

    total_salary = 0

    for employee in employees:

        total_salary += employee.salary

    return total_salary / len(employees)


def get_highest_salary(employees):

    if not employees:
        return None

    highest_salary = employees[0].salary

    for employee in employees:

        if employee.salary > highest_salary:

            highest_salary = employee.salary

    return highest_salary