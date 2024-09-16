from functools import cache
from typing import Literal

from environs import Env
from marshmallow.validate import OneOf


class AppConfig:
    def __init__(self) -> None:
        _env = Env()
        _env.read_env()
        self.db_name: str = _env("DB_NAME")
        self.db_pwd: str = _env("DB_PWD", "")
        self.db_user: str = _env("DB_USER", "")
        self.db_host: str = _env("DB_HOST", "")
        self.db_type: Literal["POSTGRES", "SQLITE"] = _env.str(
            "DB_TYPE",
            default="POSTGRES",
            validate=OneOf(["POSTGRES", "SQLITE"]),
        )

    @property
    def db_dialect(self) -> str:
        if self.db_type == "POSTGRES":
            return "postgresql+psycopg"
        return "sqlite"

    @property
    def db_url(self) -> str:
        if self.db_user and self.db_pwd:
            db_user_info = f"{self.db_user}:{self.db_pwd}"
        else:
            db_user_info = self.db_user

        if self.db_host and db_user_info:
            conn_info = f"{db_user_info}@{self.db_host}"
        else:
            conn_info = ""
        return f"{self.db_dialect}://{conn_info}/{self.db_name}"


@cache
def get_config() -> AppConfig:
    return AppConfig()
