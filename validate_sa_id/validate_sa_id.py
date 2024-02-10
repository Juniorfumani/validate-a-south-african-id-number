from datetime import datetime


def is_id_number_date_of_birth_valid(year, month, day):
    try:
        year, month, day = int(year), int(month), int(day)
        date_object = datetime(year=year, month=month, day=day)
        return True
    except ValueError:
        raise ValueError("Invalid date. Please provide a valid date.")


def is_id_number_gender_valid(gender):
    if not 0 <= gender <= 9999:
        raise ValueError("Invalid gender. Gender should be a 4-digit number.")
    return True


def is_id_number_citizenship_valid(citizenship):
    citizenship = int(citizenship)
    if citizenship not in (0, 1):
        raise ValueError("Invalid citizenship value. Should be either 0 or 1.")
    return True


def is_id_number_checksum_valid(id_number):
    if not id_number.isdigit():
        raise ValueError(
            "Invalid characters in ID number. ID number should contain only digits."
        )

    digits = [int(digit) for digit in reversed(id_number)]
    doubled_digits = [
        digit * 2 if index % 2 == 1 else digit for index, digit in enumerate(digits)
    ]
    summed_digits = [digit - 9 if digit > 9 else digit for digit in doubled_digits]
    total = sum(summed_digits)

    if total % 10 != 0:
        raise ValueError("Invalid checksum. ID number failed checksum validation.")
    return True


def is_id_number_length_valid(id_number):
    if len(id_number) != 13:
        raise ValueError("Invalid ID number length. ID number should be 13 digits.")
    return True


def is_id_number_made_up_of_only_digits(id_number):
    if not id_number.isnumeric():
        raise ValueError(
            "Invalid characters in ID number. ID number should contain only digits."
        )
    return True


def is_argument_id_number_a_string(id_number):
    if not isinstance(id_number, str):
        raise TypeError("ID number must be a string.")
    return True


def is_id_number_valid(id_number):
    try:
        is_argument_id_number_a_string(id_number)

        if not is_id_number_length_valid(
            id_number
        ) and is_id_number_made_up_of_only_digits(id_number):
            return False

        current_year = datetime.now().year % 100
        birth_year = int(id_number[:2])

        if birth_year > current_year:
            birth_year += 1900
        else:
            birth_year += 2000

        month = int(id_number[2:4])
        day = int(id_number[4:6])
        gender = int(id_number[6:10])
        citizenship = int(id_number[10])

        is_id_number_date_of_birth_valid(birth_year, month, day)
        is_id_number_gender_valid(gender)
        is_id_number_citizenship_valid(citizenship)
        is_id_number_checksum_valid(id_number)

        return True
    except (TypeError, ValueError) as e:
        return False
