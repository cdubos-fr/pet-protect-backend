import datetime
import uuid
from enum import Enum

import sqlalchemy as sa
from sqlmodel import Column
from sqlmodel import Field
from sqlmodel import Relationship
from sqlmodel import SQLModel

from .organization import Organization


class Species(str, Enum):
    CAT = "Cat"
    DOG = "Dog"
    RABBIT = "Rabbit"


class Animal(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    owner_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        foreign_key="organization.id",
    )
    owner: "Organization" = Relationship(back_populates="animals")
    species: Species = Field(sa_column=Column(sa.Enum(Species), nullable=False))
    birthday: datetime.date
    description: str
