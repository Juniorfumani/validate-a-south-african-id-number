import pytest

from validate_sa_id.validate_sa_id import (
    is_argument_id_number_a_string,
    is_id_number_date_of_birth_valid,
    is_id_number_gender_valid,
    is_id_number_citizenship_valid,
    is_id_number_checksum_valid,
    is_id_number_length_valid,
    is_id_number_made_up_of_only_digits,
)


@pytest.mark.parametrize(
    "id_number, expected_result",
    [
        ("1234567890123", True),
        ("A12345678901", True),
    ],
)
def test_is_id_number_input_valid_returns_true(id_number, expected_result):
    assert is_argument_id_number_a_string(id_number) is expected_result


@pytest.mark.parametrize(
    "year, month, day, expected_result",
    [
        (2022, 1, 15, True),
        (2000, 12, 31, True),
        (2022, 6, 15, True),
    ],
)
def test_is_id_number_date_of_birth_valid_returns_true(
    year, month, day, expected_result
):
    assert is_id_number_date_of_birth_valid(year, month, day) is expected_result


@pytest.mark.parametrize(
    "gender, expected_result",
    [
        (1234, True),
        (9999, True),
    ],
)
def test_is_id_number_gender_valid_returns_true(gender, expected_result):
    assert is_id_number_gender_valid(gender) is expected_result


@pytest.mark.parametrize(
    "citizenship, expected_result",
    [
        (0, True),
        (1, True),
    ],
)
def test_is_id_number_citizenship_valid_returns_true(citizenship, expected_result):
    assert is_id_number_citizenship_valid(citizenship) == expected_result


@pytest.mark.parametrize(
    "id_number, expected_result",
    [
        ("9406125609081", True),
        ("0505020617088", True),
    ],
)
def test_is_id_number_checksum_valid_returns_true(id_number, expected_result):
    assert is_id_number_checksum_valid(id_number) == expected_result


@pytest.mark.parametrize(
    "id_number, expected_result",
    [
        ("2001014800086", True),
        ("9406125609081", True),
    ],
)
def test_is_id_number_length_valid_returns_true(id_number, expected_result):
    assert is_id_number_length_valid(id_number) == expected_result


@pytest.mark.parametrize(
    "year, month, day, test_name",
    [
        (2022, 13, 15, "invalid_date_1"),
        (2000, 2, 35, "invalid_date_2"),
    ],
)
def test_is_id_number_date_of_birth_valid_with_invalid_input_raises_error(
    year, month, day, test_name
):
    with pytest.raises(ValueError, match="Invalid date. Please provide a valid date."):
        is_id_number_date_of_birth_valid(year, month, day)


@pytest.mark.parametrize(
    "gender, test_name",
    [
        (-1, "invalid_gender_1"),
        (10000, "invalid_gender_2"),
    ],
)
def test_is_id_number_gender_valid_with_invalid_input_raises_error(gender, test_name):
    with pytest.raises(
        ValueError, match="Invalid gender. Gender should be a 4-digit number."
    ):
        is_id_number_gender_valid(gender)


@pytest.mark.parametrize(
    "citizenship, test_name",
    [
        (2, "invalid_citizenship_1"),
        (-1, "invalid_citizenship_2"),
        (3, "invalid_citizenship_3"),
    ],
)
def test_is_id_number_citizenship_valid_with_invalid_input_raises_error(
    citizenship, test_name
):
    with pytest.raises(
        ValueError, match="Invalid citizenship value. Should be either 0 or 1."
    ):
        is_id_number_citizenship_valid(citizenship)


@pytest.mark.parametrize(
    "id_number, test_name",
    [
        ("9406125609082", "invalid_checksum_1"),
        ("9406125609084", "invalid_checksum_2"),
    ],
)
def test_is_id_number_checksum_valid_with_invalid_input_raises_error(
    id_number, test_name
):
    with pytest.raises(
        ValueError, match="Invalid checksum. ID number failed checksum validation."
    ):
        is_id_number_checksum_valid(id_number)


@pytest.mark.parametrize(
    "id_number, test_name",
    [
        (1234567890123, "invalid_input_type_1"),
        (None, "invalid_input_type_2"),
    ],
)
def test_is_argument_id_number_a_string_with_invalid_input_raises_error(
    id_number, test_name
):
    with pytest.raises(TypeError, match="ID number must be a string."):
        is_argument_id_number_a_string(id_number)


@pytest.mark.parametrize(
    "id_number, test_name",
    [
        ("94061256090812132", "invalid_id_number_length_1"),
        ("940612560", "invalid_id_number_length_2"),
    ],
)
def test_is_id_number_length_valid_with_invalid_input_raises_error(
    id_number, test_name
):
    with pytest.raises(
        ValueError, match="Invalid ID number length. ID number should be 13 digits."
    ):
        is_id_number_length_valid(id_number)


@pytest.mark.parametrize(
    "id_number, test_name",
    [
        ("2001A1-400wta", "invalid_character_input_1"),
        ("2001A14800086", "invalid_character_input_2"),
    ],
)
def test_is_id_number_made_up_of_only_digits_with_invalid_input_raises_error(
    id_number, test_name
):
    with pytest.raises(
        ValueError,
        match="Invalid characters in ID number. ID number should contain only digits.",
    ):
        is_id_number_made_up_of_only_digits(id_number)
