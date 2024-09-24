from sqlalchemy.future.engine import Engine
from sqlmodel import Session

from pet_protect_backend.conn import db_session
from pet_protect_backend.conn import get_engine


class TestConn:
    def test_get_engine(self, sqlite_db_info: None) -> None:
        engine = get_engine()
        assert isinstance(engine, Engine)

    def test_session(self, sqlite_db_info: None) -> None:
        with db_session() as session:
            assert isinstance(session, Session)
