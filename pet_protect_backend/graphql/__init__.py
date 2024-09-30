"""GraphQL module, define graphql operation (query, mutation ...) and schema."""

from ._schema import Query
from ._schema import schema

__all__ = ['schema', 'Query']
