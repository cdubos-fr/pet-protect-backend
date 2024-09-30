import strawberry

from pet_protect_backend.models import Animal


@strawberry.experimental.pydantic.type(model=Animal, all_fields=True)
class AnimalType:
    pass
