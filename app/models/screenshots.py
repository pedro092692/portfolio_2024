from app.extensions import db, Integer, String, relationship, Mapped, mapped_column, List, ForeignKey
from app.models.helpers import add_item, update_item, delete_item


class ScreenShot(db.Model):
    __tablename__ = "screenshots"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    work_id: Mapped[int] = mapped_column(Integer, ForeignKey("works.id", ondelete="CASCADE"))
    img_url: Mapped[str] = mapped_column(String(2000), nullable=False)
    work: Mapped["Work"] = relationship(back_populates="screenshots")

    @staticmethod
    def add_screenshot(*args):
        return add_item(ScreenShot, *args)

    @staticmethod
    def update_screenshot(obj_item, *args):
        return update_item(obj_item, *args)

    @staticmethod
    def delete_screenshot(obj_item):
        return delete_item(obj_item)


