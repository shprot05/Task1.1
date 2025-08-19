from pathlib import Path
from pydantic_settings import BaseSettings

from pydantic import BaseModel, SecretStr


CURRENT_FILE_PATH = Path(__file__)
BASE_DIR = CURRENT_FILE_PATH.parent
ENV_FILE_PATH = BASE_DIR / ".env"


class DBSettings(BaseModel):
    host: str
    user: str
    password: SecretStr
    port: int
    name: str


class Settings(BaseSettings, env_nested_delimiter="_"):
    db: DBSettings


def load_settings(env_file) -> Settings:
    return Settings(_env_file=env_file)


