from sqlmodel import Session
from sqlmodel import select

from pet_protect_backend.graphql import schema
from pet_protect_backend.models import Animal


class TestAnimalsQuery:
    def test_query(self, cat: Animal, session: Session) -> None:
        values = session.exec(select(Animal.id)).all()

        query = """
            query TestQuery {
                animals {
                    id
                }
            }
        """

        result = schema.execute_sync(
            query,
        )
        assert result.errors is None
        assert result.data is not None
        assert len(result.data) > 0
        assert [d['id'] for d in result.data['animals']] == [str(v) for v in values]
        assert cat.id in values
