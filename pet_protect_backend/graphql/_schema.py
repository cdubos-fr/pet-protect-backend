from collections.abc import Callable
from collections.abc import Sequence

import strawberry
from sqlmodel import SQLModel
from sqlmodel import select

from pet_protect_backend.conn import db_session
from pet_protect_backend.models import Animal
from pet_protect_backend.models import Organization

from .types import AnimalType
from .types import OrganizationType


def resolver[T: SQLModel](db_type: type[T]) -> Callable[[], Sequence[T]]:
    def _resolver() -> Sequence[T]:
        with db_session() as session:
            return session.exec(select(db_type)).all()

    return _resolver


@strawberry.type
class Query:
    animals: list[AnimalType] = strawberry.field(resolver=resolver(Animal))  # type: ignore[assignment]
    organizations: list[OrganizationType] = strawberry.field(resolver=resolver(Organization))  # type: ignore[assignment]


schema = strawberry.Schema(query=Query)
