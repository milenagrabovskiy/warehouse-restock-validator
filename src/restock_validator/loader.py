"""
This module contains a function that loads restock manifesto data from a json file.
Custom exceptions from exceptions.py are raised if issues loading data are encountered.
"""
from json import JSONDecodeError
from pathlib import Path
from pydantic import ValidationError
import json

from restock_validator.config import AppSettings
from restock_validator.exceptions import WarehouseDataNotFoundError, InvalidWarehouseDataFormatError
from restock_validator.models import RestockItem


def load_manifest(path: Path | None = None) -> tuple[list[RestockItem], list[dict]]:

    manifesto_path = path if path is not None else AppSettings().manifest_path

    try:
        text = manifesto_path.read_text(encoding="utf-8")
    except FileNotFoundError as e:
        raise WarehouseDataNotFoundError(f"No data file found at: {manifesto_path}") from e


    try:
        manifesto_rows = json.loads(text)
    except JSONDecodeError as e:
        raise InvalidWarehouseDataFormatError(f"Unable to load data from {manifesto_path} due to formatting issues") from e


    valid_rows = []
    invalid_rows = []

    for row in manifesto_rows:
        try:
            valid_rows.append(RestockItem.model_validate(row))
        except ValidationError as e:
            error_messages = [f"{e['loc']}: {e['msg']}" for e in e.errors()]
            invalid_rows.append({"id": row.get("id", "no_id"), "errors": error_messages})

    return valid_rows, invalid_rows
