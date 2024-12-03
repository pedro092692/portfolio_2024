from app.extensions import db, Integer, String, relationship, Mapped, mapped_column, List, ForeignKey
from app.models.work import Work


class ScreenShot(db.Model):
    __tablename__ = "screenshots"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    work_id: Mapped[int] = mapped_column(Integer, ForeignKey("works.id", ondelete="CASCADE"))
    img_url: Mapped[str] = mapped_column(String(300), nullable=False)
    work: Mapped["Work"] = relationship(back_populates="screenshots")


