import uuid
from datetime import date

from sqlmodel import Session
from sqlmodel import select

from pet_protect_backend.models import Animal
from pet_protect_backend.models import Organization
from pet_protect_backend.models import Species


class TestAnimal:
    def test_instance(self, cat: Animal, asso: Organization) -> None:
        assert isinstance(cat.id, uuid.UUID)
        assert cat.name == 'Cutti'
        assert cat.description == 'A cutti kitty cat'
        assert cat.owner == asso
        assert cat.birthday == date(year=2023, month=5, day=15)
        assert cat.species == Species.CAT

    def test_select_instance(self, session: Session, cat: Animal) -> None:
        animal = session.exec(select(Animal)).first()
        assert animal is not None
        assert animal.id == cat.id
        assert animal.name == cat.name
        assert animal.description == cat.description
        assert animal.owner_id == cat.owner_id
        assert animal.birthday == cat.birthday
        assert animal.species == cat.species
