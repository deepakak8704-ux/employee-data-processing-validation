import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee(
            101,
            "Rahul",
            "IT",
            45000,
            "rahul@gmail.com"
        )

    def test_employee_creation(self):
        self.assertEqual(self.employee.employee_id, 101)
        self.assertEqual(self.employee.name, "Rahul")
        self.assertEqual(self.employee.department, "IT")
        self.assertEqual(self.employee.salary, 45000)

    def test_annual_salary(self):
        self.assertEqual(
            self.employee.get_annual_salary(),
            540000
        )

    def test_salary_update(self):
        result = self.employee.update_salary(50000)

        self.assertTrue(result)
        self.assertEqual(self.employee.salary, 50000)

    def test_reject_invalid_salary(self):
        result = self.employee.update_salary(-1000)

        self.assertFalse(result)
        self.assertEqual(self.employee.salary, 45000)

    def test_department_update(self):
        result = self.employee.update_department("HR")

        self.assertTrue(result)
        self.assertEqual(self.employee.department, "HR")

    def test_email_update(self):
        result = self.employee.update_email("new@gmail.com")

        self.assertTrue(result)
        self.assertEqual(self.employee.email, "new@gmail.com")

    def test_invalid_email_update(self):
        result = self.employee.update_email("invalid-email")

        self.assertFalse(result)
        self.assertEqual(self.employee.email, "rahul@gmail.com")

    def test_employee_is_valid(self):
        self.assertTrue(self.employee.is_valid())

    def test_to_dict(self):
        data = self.employee.to_dict()

        self.assertEqual(data["employee_id"], 101)
        self.assertEqual(data["name"], "Rahul")
        self.assertEqual(data["salary"], 45000)

    def test_salary_grade(self):
        self.assertEqual(self.employee.get_salary_grade(), "B")


if __name__ == "__main__":
    unittest.main()