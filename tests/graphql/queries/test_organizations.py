from sqlmodel import Session
from sqlmodel import select

from pet_protect_backend.graphql import schema
from pet_protect_backend.models import Organization


class TestOrganizationsQuery:
    def test_query(self, asso: Organization, session: Session) -> None:
        values = session.exec(select(Organization.id)).all()

        query = """
            query TestQuery {
                organizations {
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
        assert [d['id'] for d in result.data['organizations']] == [str(v) for v in values]
        assert asso.id in values
