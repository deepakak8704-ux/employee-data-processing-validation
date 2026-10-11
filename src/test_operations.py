import unittest

from employee import Employee
from search import search_by_id, search_by_name
from filter import filter_by_department
from statistics import (
    get_employee_count,
    get_department_counts,
    get_average_salary,
    get_highest_salary
)


class TestEmployeeOperations(unittest.TestCase):

    def setUp(self):
        self.employees = [
            Employee(101, "Rahul", "IT", 45000, "rahul@gmail.com"),
            Employee(102, "Anita", "HR", 38000, "anita@gmail.com"),
            Employee(103, "John", "IT", 52000, "john@gmail.com")
        ]

    def test_search_by_id(self):
        result = search_by_id(self.employees, 101)
        self.assertEqual(result.name, "Rahul")

    def test_search_missing_id(self):
        result = search_by_id(self.employees, 999)
        self.assertIsNone(result)

    def test_search_by_name(self):
        result = search_by_name(self.employees, "anita")
        self.assertEqual(result.employee_id, 102)

    def test_search_missing_name(self):
        result = search_by_name(self.employees, "David")
        self.assertIsNone(result)

    def test_filter_by_department(self):
        result = filter_by_department(self.employees, "IT")
        self.assertEqual(len(result), 2)

    def test_department_filter_is_case_insensitive(self):
        result = filter_by_department(self.employees, "hr")
        self.assertEqual(result[0].name, "Anita")

    def test_employee_count(self):
        self.assertEqual(get_employee_count(self.employees), 3)

    def test_department_counts(self):
        result = get_department_counts(self.employees)
        self.assertEqual(result, {"IT": 2, "HR": 1})

    def test_average_salary(self):
        self.assertAlmostEqual(
            get_average_salary(self.employees),
            45000
        )

    def test_highest_salary(self):
        self.assertEqual(
            get_highest_salary(self.employees),
            52000
        )

    def test_statistics_for_empty_list(self):
        self.assertEqual(get_average_salary([]), 0)
        self.assertIsNone(get_highest_salary([]))


if __name__ == "__main__":
    unittest.main()