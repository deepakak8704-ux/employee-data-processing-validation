import unittest
import os
import tempfile

from report import generate_quality_report, save_quality_report


class TestQualityReport(unittest.TestCase):

    def setUp(self):
        self.valid_employees = [
            {
                "employee_id": 101,
                "name": "Rahul",
                "department": "IT",
                "salary": 45000,
                "email": "rahul@gmail.com"
            },
            {
                "employee_id": 102,
                "name": "Anita",
                "department": "HR",
                "salary": 38000,
                "email": "anita@gmail.com"
            }
        ]

        self.validation_errors = [
            {
                "employee_id": 101,
                "errors": ["Duplicate employee ID"]
            },
            {
                "employee_id": 103,
                "errors": ["Invalid salary", "Invalid email"]
            }
        ]

    def test_report_totals(self):
        report = generate_quality_report(
            self.valid_employees,
            self.validation_errors
        )

        self.assertEqual(report["total_records"], 4)
        self.assertEqual(report["valid_records"], 2)
        self.assertEqual(report["invalid_records"], 2)
        self.assertEqual(report["total_errors"], 3)

    def test_error_counts(self):
        report = generate_quality_report(
            self.valid_employees,
            self.validation_errors
        )

        self.assertEqual(
            report["error_counts"]["Duplicate Employee ID"], 1
        )
        self.assertEqual(
            report["error_counts"]["Invalid Salary"], 1
        )
        self.assertEqual(
            report["error_counts"]["Invalid Email"], 1
        )

    def test_save_quality_report(self):
        report = generate_quality_report(
            self.valid_employees,
            self.validation_errors
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            filename = os.path.join(temp_dir, "report.txt")

            save_quality_report(report, filename)

            self.assertTrue(os.path.exists(filename))

            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()

            self.assertIn("Total Records: 4", content)
            self.assertIn("Valid Records: 2", content)
            self.assertIn("Invalid Records: 2", content)
            self.assertIn("Total Errors: 3", content)


if __name__ == "__main__":
    unittest.main()