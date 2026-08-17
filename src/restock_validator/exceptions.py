"""
Module of customer exception classes to raise if problems with loading data file are encountered
"""

class WarehouseValidatorError(Exception):
    """Base exception class for any exceptions that occur while loading data"""

class WarehouseDataNotFoundError(WarehouseValidatorError):
    """raise this exception when the warehouse data file does not exist"""

class InvalidWarehouseDataFormatError(WarehouseValidatorError):
    """raise this exception when warehouse data file cannot be loaded due to improper formatting"""