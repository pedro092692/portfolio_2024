from app.extensions import db, Mapped, mapped_column, Integer, String, relationship, List, Boolean
from app.models.helpers import add_item, get_item, update_item, delete_item


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
    work_category: Mapped[str] = mapped_column(String, nullable=False)
    full_width: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    position: Mapped[int] = mapped_column(Integer, nullable=True)
    screenshots: Mapped[List["ScreenShot"]] = relationship(back_populates="work",  cascade="all,delete")
    slug: Mapped[str] = mapped_column(String, unique=True, nullable=True)

    @staticmethod
    def add_work(*args):
        return add_item(Work, *args)

    @staticmethod
    def get_works():
        works = db.session.query(Work).order_by(Work.position).all()
        return works

    @staticmethod
    def get_work(work_id):
        return get_item(Work, work_id)

    @staticmethod
    def update_work(obj_item, *args):
        return update_item(obj_item, *args)

    @staticmethod
    def delete_work(work_obj):
        return delete_item(work_obj)

    @staticmethod
    def check_slug(slug):
        return Work.query.filter_by(slug=slug).first()
