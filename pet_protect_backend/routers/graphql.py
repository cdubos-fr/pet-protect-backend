"""GraphQL router definition."""

from strawberry.fastapi import GraphQLRouter

from pet_protect_backend.graphql import schema

router: GraphQLRouter = GraphQLRouter(schema)  # type: ignore[type-arg]
