
# Project Description

## Project Title
Employee Data Processing & Validation System

## Objective
To develop a Python application that reads employee records from CSV and JSON files, validates employee information, processes valid records, and generates a data-quality report.

## Features
- Load employee records from CSV and JSON files.
- Validate employee ID, name, department, salary, and email.
- Identify missing fields, invalid values, and duplicate employee IDs.
- Search employees by ID or name.
- Filter employees by department.
- Calculate total employee count, department-wise count, average salary, and highest salary.
- Save validated employee records in CSV and JSON formats.
- Generate a data-quality report.
- Handle file-related errors and log application events.
- Run automated unit tests.

## Technologies and Concepts Used
- Python
- Lists, dictionaries, and functions
- Modular programming
- CSV and JSON file handling
- Data validation
- Exception handling
- Object-oriented programming
- Logging
- Unit testing

## How to Run
1. Install Python 3.10 or later.
2. Clone or download the GitHub repository.
3. Open the project folder in a terminal.
4. Run the application:

   `python src/main.py`

## How to Run Tests
Execute:

`python -m unittest discover -s src -p "test_*.py" -v`

## Repository
https://github.com/deepakak8704-ux/employee-data-processing-validation

## Conclusion
This project demonstrates the use of Python to validate and process employee data, identify data-quality issues, generate useful statistics, and save processed records for further use.
