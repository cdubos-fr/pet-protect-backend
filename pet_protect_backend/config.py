from functools import cache

from environs import Env


_env = Env()
_env.read_env()


class AppConfig:
    db_name: str = _env("DB_NAME")
    db_pwd: str = _env("DB_PWD")
    db_user: str = _env("DB_USER")
    db_host: str = _env("DB_HOST")
    dialect = "postgresql+psycopg"

    @property
    def db_url(self) -> str:
        return f"{self.dialect}://{self.db_user}:{self.db_pwd}@{self.db_host}/{self.db_name}"


@cache
def get_config() -> AppConfig:
    return AppConfig()
