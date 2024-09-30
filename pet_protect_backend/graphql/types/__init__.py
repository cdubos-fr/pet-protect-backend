"""GraphQL type module, define type accessible for graphql queries and mutations."""

from ._animal import AnimalType
from ._organization import OrganizationType

__all__ = [
    'AnimalType',
    'OrganizationType',
]
