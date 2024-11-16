from sqlalchemy import select

from app.api.schemas.health import AddHealthStateSchema
from app.database.models.health import HealthStateOrm
from app.utils.repository import AbsRepo



class HealthStateRepository(AbsRepo):
    async def add_one(self, data: AddHealthStateSchema) -> None:
        health = HealthStateOrm(**data.model_dump())
        self.session.add(health)
        await self.session.commit()

    async def get_all_health_states(self) -> HealthStateOrm:
        query = select(HealthStateOrm)
        return await self.session.scalars(query)
