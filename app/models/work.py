from app.extensions import db, Mapped, mapped_column, Integer, String, relationship
from app.models.helpers import add_item


class Work(db.Model):
    __tablename__ = "works"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False)
    subtitle: Mapped[str] = mapped_column(String(150), nullable=False)
    technology: Mapped[str] = mapped_column(String(150), nullable=False)
    image_url: Mapped[str] = mapped_column(String(150), nullable=False)

