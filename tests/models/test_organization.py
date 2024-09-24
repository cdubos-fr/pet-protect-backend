import uuid

from sqlmodel import Session
from sqlmodel import select

from pet_protect_backend.models import Animal
from pet_protect_backend.models import Organization


class TestOrganization:
    def test_instance(self, cat: Animal, asso: Organization) -> None:
        assert isinstance(asso.id, uuid.UUID)
        assert asso.name == 'Cat Asso'
        assert cat in asso.animals

    def test_select_instance(self, session: Session, asso: Organization) -> None:
        org = session.exec(select(Organization)).first()
        assert org is not None
        assert org.id == asso.id
        assert org.name == asso.name
