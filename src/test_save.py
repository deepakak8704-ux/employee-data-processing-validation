import unittest
import os
import csv
import json
import tempfile

from employee import Employee
from save import save_valid_employees
from json_save import save_employees_json


class TestEmployeeSaving(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()

        self.csv_path = os.path.join(
            self.temp_dir.name, "employees.csv"
        )
        self.json_path = os.path.join(
            self.temp_dir.name, "employees.json"
        )

        self.employees = [
            Employee(
                101, "Rahul", "IT", 45000,
                "rahul@gmail.com"
            ),
            Employee(
                102, "Anita", "HR", 38000,
                "anita@gmail.com"
            )
        ]

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_save_csv(self):
        save_valid_employees(
            self.employees, self.csv_path
        )

        self.assertTrue(os.path.exists(self.csv_path))

        with open(
            self.csv_path, "r", encoding="utf-8"
        ) as file:
            rows = list(csv.DictReader(file))

        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["name"], "Rahul")
        self.assertEqual(rows[1]["department"], "HR")

    def test_save_json(self):
        save_employees_json(
            self.employees, self.json_path
        )

        self.assertTrue(os.path.exists(self.json_path))

        with open(
            self.json_path, "r", encoding="utf-8"
        ) as file:
            data = json.load(file)

        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["employee_id"], 101)
        self.assertEqual(data[0]["salary"], 45000)

    def test_json_contains_all_employee_fields(self):
        save_employees_json(
            self.employees, self.json_path
        )

        with open(
            self.json_path, "r", encoding="utf-8"
        ) as file:
            data = json.load(file)

        expected_fields = {
            "employee_id",
            "name",
            "department",
            "salary",
            "email"
        }

        self.assertEqual(set(data[0].keys()), expected_fields)

    def test_save_empty_csv(self):
        save_valid_employees([], self.csv_path)
        self.assertFalse(os.path.exists(self.csv_path))

    def test_save_empty_json(self):
        save_employees_json([], self.json_path)
        self.assertFalse(os.path.exists(self.json_path))


if __name__ == "__main__":
    unittest.main()