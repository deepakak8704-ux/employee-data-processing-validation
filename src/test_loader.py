
import unittest
import json
import os
import tempfile

from loader import load_csv, load_json, load_employees


class TestEmployeeLoader(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()

        self.csv_path = os.path.join(
            self.temp_dir.name,
            "employees.csv"
        )

        self.json_path = os.path.join(
            self.temp_dir.name,
            "employees.json"
        )

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_load_valid_csv(self):
        with open(
            self.csv_path,
            "w",
            encoding="utf-8"
        ) as file:
            file.write(
                "employee_id,name,department,salary,email\n"
                "101,Rahul,IT,45000,rahul@gmail.com\n"
            )

        employees = load_csv(self.csv_path)

        self.assertEqual(len(employees), 1)
        self.assertEqual(employees[0]["name"], "Rahul")

    def test_load_valid_json(self):
        data = [
            {
                "employee_id": 101,
                "name": "Rahul",
                "department": "IT",
                "salary": 45000,
                "email": "rahul@gmail.com"
            }
        ]

        # Write one employee to a temporary JSON file
        with open(
            self.json_path,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(data, file, indent=4)

        # DEBUG 1: Read back the actual file contents
        with open(
            self.json_path,
            "r",
            encoding="utf-8"
        ) as file:
            saved_data = json.load(file)

        print("\nDEBUG - JSON file contents:", saved_data)
        print("DEBUG - JSON file path:", self.json_path)

        # Load records using the actual loader function
        employees = load_json(self.json_path)

        # DEBUG 2: Inspect the loader's returned records
        print("DEBUG - Loader returned:", employees)
        print("DEBUG - Number of employees:", len(employees))

        # Assertions
        self.assertEqual(len(employees), 1)
        self.assertEqual(employees[0]["employee_id"], 101)
        self.assertEqual(employees[0]["name"], "Rahul")

    def test_csv_missing_required_column(self):
        with open(
            self.csv_path,
            "w",
            encoding="utf-8"
        ) as file:
            file.write(
                "employee_id,name\n"
                "101,Rahul\n"
            )

        with self.assertRaises(ValueError):
            load_csv(self.csv_path)

    def test_json_must_contain_list(self):
        with open(
            self.json_path,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump({"name": "Rahul"}, file)

        with self.assertRaises(ValueError):
            load_json(self.json_path)

    def test_json_record_must_be_dictionary(self):
        with open(
            self.json_path,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(["Rahul"], file)

        with self.assertRaises(ValueError):
            load_json(self.json_path)

    def test_missing_file(self):
        missing_path = os.path.join(
            self.temp_dir.name,
            "missing.csv"
        )

        result = load_employees(missing_path)

        self.assertIsNone(result)

    def test_unsupported_file_format(self):
        unsupported_path = os.path.join(
            self.temp_dir.name,
            "employees.txt"
        )

        result = load_employees(unsupported_path)

        self.assertIsNone(result)

    def test_invalid_json_file(self):
        with open(
            self.json_path,
            "w",
            encoding="utf-8"
        ) as file:
            file.write("{invalid json}")

        result = load_employees(self.json_path)

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()