from app.extensions import db, Integer, String, DateTime, Mapped, mapped_column, datetime
from app.models.helpers import add_item


class Message(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(150), nullable=False)
    name: Mapped[str] =  mapped_column(String(150), nullable=False)
    subject: Mapped[str] = mapped_column(String(100), nullable=False)
    message: Mapped[str] = mapped_column(String(500), nullable=False)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now())


