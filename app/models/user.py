from app.extensions import db
from app.models.helpers import add_item


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    password = db.Column(db.String(200))
    role = db.Column(db.String(20))

    def __repr__(self):
        return f'<User "{self.email}">'

    @staticmethod
    def create_user(*args):
        return add_item(User, *args)

    @staticmethod
    def get_user_id(user_id):
        user = db.session.execute(db.select(User).filter(User.id == user_id)).scalar()
        return user


