import uuid
from typing import TYPE_CHECKING

from sqlmodel import Field
from sqlmodel import Relationship
from sqlmodel import SQLModel

if TYPE_CHECKING:  # pragma: no cover
    from pet_protect_backend.models import Animal


class Organization(SQLModel, table=True):
    """Model to represent Organization (association, enterprise, ...)."""

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(index=True)
    animals: list['Animal'] = Relationship(back_populates='owner')
