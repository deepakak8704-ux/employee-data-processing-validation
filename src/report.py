def generate_quality_report(
    employees,
    validation_errors
):

    total_records = (
        len(employees)
        + len(validation_errors)
    )

    valid_records = len(employees)

    invalid_records = len(
        validation_errors
    )

    total_errors = 0

    for error in validation_errors:

        total_errors += len(
            error["errors"]
        )

    error_counts = {}

    for error in validation_errors:

        for message in error["errors"]:

            if message.startswith(
                "Missing fields"
            ):

                error_type = "Missing Fields"

            elif message == "Invalid employee ID":

                error_type = "Invalid Employee ID"

            elif message == "Duplicate employee ID":

                error_type = "Duplicate Employee ID"

            elif message == "Invalid name":

                error_type = "Invalid Name"

            elif message == "Invalid department":

                error_type = "Invalid Department"

            elif message == "Invalid salary":

                error_type = "Invalid Salary"

            elif message == "Invalid email":

                error_type = "Invalid Email"

            else:

                error_type = "Other"

            if error_type in error_counts:

                error_counts[error_type] += 1

            else:

                error_counts[error_type] = 1

    return {
        "total_records": total_records,
        "valid_records": valid_records,
        "invalid_records": invalid_records,
        "total_errors": total_errors,
        "error_counts": error_counts
    }


def save_quality_report(report, filename):

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "DATA QUALITY REPORT\n"
        )

        file.write(
            "==================\n\n"
        )

        file.write(
            f"Total Records: "
            f"{report['total_records']}\n"
        )

        file.write(
            f"Valid Records: "
            f"{report['valid_records']}\n"
        )

        file.write(
            f"Invalid Records: "
            f"{report['invalid_records']}\n"
        )

        file.write(
            f"Total Errors: "
            f"{report['total_errors']}\n"
        )

        file.write(
            "\nError Summary\n"
        )

        file.write(
            "-------------\n"
        )

        for error, count in report[
            "error_counts"
        ].items():

            file.write(
                f"{error}: {count}\n"
            )