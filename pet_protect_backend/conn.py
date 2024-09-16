from collections.abc import Generator
from contextlib import contextmanager

from sqlalchemy.future.engine import Engine
from sqlmodel import create_engine
from sqlmodel import Session

from pet_protect_backend.config import get_config


def get_engine() -> Engine:
    config = get_config()
    return create_engine(
        config.db_url,
        connect_args={
            "check_same_thread": False,
        }
        if config.db_type == "SQLITE"
        else {},
    )


@contextmanager
def db_session() -> Generator[Session, None, None]:
    yield Session(get_engine())
