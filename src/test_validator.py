import unittest

from validator import (
    validate_required_fields,
    validate_employee_id,
    validate_salary,
    validate_name,
    validate_department,
    validate_email
)


class TestEmployeeValidator(unittest.TestCase):

    def test_valid_employee_id(self):
        self.assertTrue(validate_employee_id("101"))

    def test_invalid_employee_id(self):
        self.assertFalse(validate_employee_id("abc"))
        self.assertFalse(validate_employee_id("0"))

    def test_valid_salary(self):
        self.assertTrue(validate_salary("45000"))

    def test_invalid_salary(self):
        self.assertFalse(validate_salary("-5000"))
        self.assertFalse(validate_salary("abc"))

    def test_valid_name(self):
        self.assertTrue(validate_name("Rahul"))

    def test_invalid_name(self):
        self.assertFalse(validate_name(""))
        self.assertFalse(validate_name("   "))

    def test_valid_department(self):
        self.assertTrue(validate_department("IT"))

    def test_invalid_department(self):
        self.assertFalse(validate_department("   "))

    def test_valid_email(self):
        self.assertTrue(validate_email("rahul@gmail.com"))

    def test_invalid_email(self):
        self.assertFalse(validate_email("ravigmail.com"))

    def test_missing_fields(self):
        employee = {
            "employee_id": "101",
            "name": "Rahul",
            "department": "IT",
            "salary": "45000"
        }

        self.assertEqual(
            validate_required_fields(employee),
            ["email"]
        )


if __name__ == "__main__":
    unittest.main()