"""
A pytest suite testing the functionality of load_tickets.

"""
import pytest
from pydantic import ValidationError
from pathlib import Path

from restock_validator.exceptions import WarehouseDataNotFoundError
from restock_validator.loader import load_manifest
from restock_validator.models import RestockItem

@pytest.fixture
def get_valid_rows():
    return load_manifest()[0]

@pytest.fixture
def get_invalid_rows():
    return load_manifest()[1]

def test_valid_rows_loaded(get_valid_rows):

    for row in get_valid_rows:
        assert isinstance(row, RestockItem), (f"Row is of unexpected type. Expected: 'RestockItem',"
                                              f"Actual: {type(row)}")


def test_invalid_rows_not_loaded(get_invalid_rows):

    for row in get_invalid_rows:
        assert not isinstance(row, RestockItem), (f"Row is of unexpected type. Expected: 'dict',"
                                              f"Actual: {type(row)}")


def test_manifest_returns_eight_valid_four_errors(get_valid_rows, get_invalid_rows):
    assert len(get_valid_rows) == 8, (f"Error. Expected: 8 valid rows,"
                                      f"Actual: {len(get_valid_rows)}")
    assert len(get_invalid_rows) == 4, (f"Error. Expected: 4 invalid rows,"
                                      f"Actual: {len(get_invalid_rows)}")


def test_missing_manifest_path_raises_exception():
    with pytest.raises(WarehouseDataNotFoundError):
        load_manifest(Path("sample.json"))  # convert string to Path obj, or you get AttributeError instead of custom error


@pytest.mark.parametrize("invalid_field, value", [
    ("category", "some_category"),  # category type not part of Literal
    ("quantity", 0),  # non-positive value
    ("unit_cost", -3.00),  # negative value
    ("warehouse", 1234)  # incorrect type (int instead of str)
])

def test_assert_invalid_fields_raise_validation_error(invalid_field, value):
    payload = {
        "sku": "SKU-1015",
        "category": "electronics",
        "warehouse": "east-6",
        "quantity": 10,
        "unit_cost": 15.00,
    }
    payload[invalid_field] = value
    with pytest.raises(ValidationError):
        RestockItem.model_validate(payload)
