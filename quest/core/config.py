# pylint: disable=too-few-public-methods
from __future__ import annotations
from logging import getLogger
from pathlib import Path
from typing import Dict, List

from pydantic_settings import BaseSettings
from pydantic_settings.main import SettingsConfigDict

logger = getLogger(__name__)


env_files: List[Path | str]
if Path(".env.prod").exists():
    logger.info("environment: production")
    env_files = [".env", ".env.prod", ".env.prod.local", ".env.secret"]
elif Path(".env.dev").exists():
    logger.info("environment: development")
    env_files = [".env", ".env.dev", ".env.dev.local", ".env.secret"]
else:
    logger.error(".env.dev | .env.prod missing, assuming we're in docker")
    env_files = []


class Config(BaseSettings):
    PROJECT_NAME: str = "quest"
    HEURIST_API: str
    HEURIST_URL: str = "https://llm-gateway.heurist.xyz"
    TEXT_MODEL: str = "hermes-3-llama3.1-8b"
    PORT: int = 8000

    model_config = SettingsConfigDict(
        env_file=env_files,
        env_nested_delimiter="__",
        extra="ignore",
    )


settings = Config.model_validate({})
