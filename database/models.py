from datetime import datetime, timezone

from sqlalchemy import Integer, Float, String, DATETIME
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

class Base(DeclarativeBase):
    pass

class Donation(Base):
    __tablename__ = 'donations'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    currency: Mapped[str] = mapped_column(String, default='RUB')
    created_at: Mapped[datetime] = mapped_column(DATETIME, default=datetime.now(timezone.utc))

    def __repr__(self):
        return f'Donat от пользователя с id {self.user_id} на сумму {self.amount}'

