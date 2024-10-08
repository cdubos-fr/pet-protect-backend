import os
from collections.abc import Generator
from datetime import date
from unittest import mock

import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session
from sqlmodel import SQLModel

from pet_protect_backend.app import app
from pet_protect_backend.config import get_config
from pet_protect_backend.conn import db_session
from pet_protect_backend.models import Animal
from pet_protect_backend.models import Organization
from pet_protect_backend.models import Species


@pytest.fixture
def sqlite_db_info() -> Generator[None, None, None]:
    with mock.patch.dict(
        os.environ,
        {'DB_TYPE': 'SQLITE', 'DB_USER': '', 'DB_HOST': '', 'DB_NAME': 'test.db'},
    ):
        get_config.cache_clear()
        yield


@pytest.fixture
def postgres_db_info() -> Generator[None, None, None]:
    with mock.patch.dict(
        os.environ,
        {
            'DB_TYPE': 'POSTGRES',
            'DB_USER': 'postgres',
            'DB_PWD': 'mypwd',
            'DB_HOST': 'localhost',
            'DB_NAME': 'test_db',
        },
    ):
        get_config.cache_clear()
        yield


@pytest.fixture
def session(sqlite_db_info: None) -> Generator[Session, None, None]:
    with db_session() as session:
        conn = session.connection()
        SQLModel.metadata.drop_all(bind=conn)
        SQLModel.metadata.create_all(bind=conn)
        yield session
    os.remove('test.db')


@pytest.fixture
def asso(session: Session) -> Organization:
    org = Organization(name='Cat Asso')
    session.add(org)
    session.commit()
    return org


@pytest.fixture
def cat(session: Session, asso: Organization) -> Animal:
    a_cutti_cat = Animal(
        name='Cutti',
        owner=asso,
        species=Species.CAT,
        description='A cutti kitty cat',
        birthday=date(year=2023, month=5, day=15),
    )
    session.add(a_cutti_cat)
    session.commit()
    return a_cutti_cat


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)
