import strawberry

from pet_protect_backend.models import Organization


@strawberry.experimental.pydantic.type(model=Organization, all_fields=True)
class OrganizationType:
    pass
