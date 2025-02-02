from random import choice
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.response import ResponseSchema
from app.api.schemas.trait import AddTraitSchema, ReadTraitSchema
from app.database.repositories.trait import TraitRepository


class TraitService:
    def __init__(self, session: AsyncSession) -> None:
        self.trait_repo = TraitRepository(session)

    async def create_trait(self, trait: AddTraitSchema) -> ResponseSchema:
        trait = await self.trait_repo.add_one(trait)
        return ResponseSchema(
            data={'trait': trait.model_dump()},
            messages=[f'Trait with id={trait.id} added successfully'],
        )

    async def get_all_traits(self) -> ResponseSchema:
        traits = await self.trait_repo.get_all()
        data = [i.model_dump() for i in traits]
        return ResponseSchema(
            data={'traits': data},
            messages=['All traits retrieved successfully'],
        )
    
    async def get_random_id(self) -> int:
        traits_id = await self.trait_repo.get_all_id()
        return choice(traits_id)
