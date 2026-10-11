
# Employee Data Processing and Validation System

## Project Overview

The Employee Data Processing and Validation System is a Python-based application that loads employee records from CSV and JSON files, validates employee information, identifies data-quality issues, and generates reports.

The application also supports employee searching, department filtering, salary statistics, and exporting validated records.

## Features

- Load employee records from CSV and JSON files.
- Validate employee IDs, names, departments, salaries, and email addresses.
- Detect missing fields and duplicate employee IDs.
- Identify invalid salary and email values.
- Generate a data quality report with error counts.
- Search employees by ID or name.
- Filter employees by department.
- Calculate employee counts, department-wise counts, average salary, and highest salary.
- Save validated records in CSV and JSON formats.
- Log application activity and validation warnings.
- Run automated unit tests using Python's unittest framework.

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- CSV and JSON
- File Handling
- Exception Handling
- Logging
- Unit Testing (`unittest`)

## Project Structure

```text
data_processing_&_validation/
├── data/
│   ├── employees.csv
│   └── employees.json
├── src/
│   ├── employee.py
│   ├── validator.py
│   ├── loader.py
│   ├── report.py
│   ├── search.py
│   ├── filter.py
│   ├── statistics.py
│   ├── save.py
│   ├── json_save.py
│   ├── logger.py
│   ├── main.py
│   └── test_*.py
├── output/
│   ├── validated_employees.csv
│   ├── validated_employees.json
│   ├── data_quality_report.txt
│   └── application.log
└── README.md
```

## Requirements

- Python 3.10 or later
- No third-party packages are required for the current implementation.

## How to Run

1. Open a terminal in the project root directory.
2. Run the application:
```bash
python src/main.py
```
3. Select CSV or JSON as the input format.
4. Review the validation report.
5. Use the menu to search employees, filter departments, or view statistics.
6. Select Exit to close the application.

## Run Automated Tests

Run all test files:

```bash
python -m unittest discover -s src -p "test_*.py" -v
```

## Sample Validation Results

Using the sample CSV dataset:

- Total records: 8
- Valid records: 3
- Invalid records: 5
- Total validation errors: 5

Detected issues include duplicate employee IDs, missing fields, invalid salaries, and invalid email addresses.

These figures describe the included sample dataset; results will vary with other input files.

## Output Files

- `validated_employees.csv` — validated employee records in CSV format.
- `validated_employees.json` — validated employee records in JSON format.
- `data_quality_report.txt` — summary of validation results.
- `application.log` — application logs and warnings.

## Learning Outcomes

This project demonstrates practical use of Python programming, modular design, object-oriented programming, data validation, file handling, exception handling, logging, reporting, and automated testing.