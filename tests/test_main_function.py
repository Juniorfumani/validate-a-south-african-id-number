import pytest

from validate_sa_id.validate_sa_id import is_id_number_valid


@pytest.mark.parametrize(
    "id_number, expected_result",
    [
        ("2001014800086", True),
        ("0010255657081", True),
        ("200101480008", False),
        ("20010148000869", False),
        ("9406125609081", True),
        ("2001014800786", False),
        ("2013514800086", False),
        ("0505020617088", True),
        ("2013001200086", False),
        ("0505020617088", True),
        ("0505210617088", True),
        ("201301480008689", False),
        ("20130148000", False),
    ],
)
def test_id_number_validity(id_number, expected_result):
    assert is_id_number_valid(id_number) == expected_result
