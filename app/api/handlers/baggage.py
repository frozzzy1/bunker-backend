from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.baggage import AddBaggageSchema
from app.api.schemas.response import ResponseSchema
from app.services.baggage import BaggageService
from app.database.database import get_session

baggages_router = APIRouter(
    prefix='/baggages',
    tags=['Baggages'],
)


@baggages_router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    response_model=ResponseSchema,
)
async def create_baggage(
    baggage: AddBaggageSchema,
    session: AsyncSession = Depends(get_session),
):
    baggage_service = BaggageService(session)
    return await baggage_service.create_baggage(baggage)
    


@baggages_router.get(
    '',
    response_model=ResponseSchema,
)
async def get_all_baggages(session: AsyncSession = Depends(get_session)):
    baggage_service = BaggageService(session)
    baggages = await baggage_service.get_all_baggages()
    return baggages
