"""
Configuration module for the project.
Maps values from .env file and provides a default path if path is not specified in .env
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


class AppSettings(BaseSettings):

    model_config = SettingsConfigDict(env_file=".env", env_prefix="RESTOCK_VALIDATOR_", extra="ignore")

    manifest_path: Path = Path(__file__).parent.parent.parent / "data" / "restock_manifest.json"
