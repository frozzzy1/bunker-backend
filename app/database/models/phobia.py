from sqlalchemy.orm import Mapped, mapped_column

from app.database.models.base import BaseOrm


class PhobiaOrm(BaseOrm):
    __tablename__ = 'phobias'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(unique=True)
