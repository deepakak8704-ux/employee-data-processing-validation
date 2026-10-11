class Employee:

    # Class variable
    company_name = "SkyCurve Technologies"

    def __init__(
        self,
        employee_id,
        name,
        department,
        salary,
        email
    ):
        # Instance variables
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary
        self.email = email

    # Display employee information
    def display_info(self):

        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(
            f"Monthly Salary: "
            f"{self.get_formatted_salary()}"
        )
        print(
            f"Annual Salary: "
            f"₹{self.get_annual_salary():,}"
        )
        print(f"Email: {self.email}")

    # Convert employee object to dictionary
    def to_dict(self):

        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "department": self.department,
            "salary": self.salary,
            "email": self.email
        }

    # Format monthly salary
    def get_formatted_salary(self):

        return f"₹{self.salary:,}"

    # Calculate annual salary
    def get_annual_salary(self):

        return self.salary * 12

    # Update salary
    def update_salary(self, new_salary):

        if new_salary <= 0:
            return False

        self.salary = new_salary

        return True

    # Update department
    def update_department(self, new_department):

        if not new_department.strip():
            return False

        self.department = new_department.strip()

        return True

    # Update email
    def update_email(self, new_email):

        new_email = new_email.strip()

        if not Employee.is_valid_email(new_email):
            return False

        self.email = new_email

        return True

    # Update employee name
    def update_name(self, new_name):

        new_name = new_name.strip()

        if not new_name:
            return False

        self.name = new_name

        return True

    # Update employee ID
    def update_employee_id(self, new_employee_id):

        if new_employee_id <= 0:
            return False

        self.employee_id = new_employee_id

        return True

    # Readable object representation
    def __str__(self):

        return (
            f"{self.employee_id} - "
            f"{self.name} - "
            f"{self.department} - "
            f"{self.get_formatted_salary()} - "
            f"{self.email}"
        )

    # Developer-friendly object representation
    def __repr__(self):

        return (
            f"Employee("
            f"employee_id={self.employee_id}, "
            f"name='{self.name}', "
            f"department='{self.department}', "
            f"salary={self.salary}, "
            f"email='{self.email}')"
        )

    # Generate employee summary
    def get_summary(self):

        return (
            f"{self.name} works in "
            f"{self.department} department "
            f"with a salary of "
            f"{self.get_formatted_salary()}."
        )

    # Return contact information
    def get_contact_info(self):

        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "email": self.email
        }

    # Validate employee object data
    def is_valid(self):

        if self.employee_id <= 0:
            return False

        if not self.name.strip():
            return False

        if not self.department.strip():
            return False

        if self.salary <= 0:
            return False

        if not Employee.is_valid_email(self.email):
            return False

        return True

    # Check department
    def has_department(self, department):

        return (
            self.department.lower()
            == department.strip().lower()
        )

    # Return formatted department label
    def get_department_label(self):

        return f"Department: {self.department}"

    # Categorize monthly salary
    def get_salary_grade(self):

        if self.salary >= 50000:
            return "A"

        elif self.salary >= 40000:
            return "B"

        else:
            return "C"

    # Check whether salary meets the high-earner threshold
    def is_high_earner(self):

        return self.salary >= 50000

    # Class method
    @classmethod
    def get_company_name(cls):

        return cls.company_name

    # Static method for basic email validation
    @staticmethod
    def is_valid_email(email):

        email = email.strip()

        if not email:
            return False

        if "@" not in email:
            return False

        if "." not in email:
            return False

        return True


# Convert employee dictionaries into Employee objects
def create_employee_objects(employees):

    employee_objects = []

    for employee in employees:

        employee_object = Employee(
            int(employee["employee_id"]),
            employee["name"],
            employee["department"],
            int(employee["salary"]),
            employee["email"]
        )

        employee_objects.append(employee_object)

    return employee_objects