from app.extensions import db, Mapped, mapped_column, Integer, String, relationship, List
from app.models.helpers import add_item, get_item, update_item


class Work(db.Model):
    __tablename__ = "works"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False)
    subtitle: Mapped[str] = mapped_column(String(150), nullable=False)
    technology: Mapped[str] = mapped_column(String(150), nullable=False)
    image_url: Mapped[str] = mapped_column(String(150), nullable=False)
    summary: Mapped[str] = mapped_column(String(500), nullable=False)
    url: Mapped[str] = mapped_column(String, nullable=True)
    repository_url: Mapped[str] = mapped_column(String, nullable=False)
    screenshots: Mapped[List["ScreenShot"]] = relationship(back_populates="work",  cascade="all,delete")

    @staticmethod
    def add_work(*args):
        return add_item(Work, *args)

    @staticmethod
    def get_works():
        works = db.session.query(Work).order_by(Work.id.desc()).all()
        return works

    @staticmethod
    def get_work(work_id):
        return get_item(Work, work_id)

    @staticmethod
    def update_work(obj_item, *args):
        return update_item(obj_item, *args)

