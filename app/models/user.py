from app.extensions import db


class User:
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    password = db.Column(db.String(200))
    role = db.Column(db.String(20))

    @staticmethod
    def get_user_id(user_id):
        user = db.session.execute(db.select(User).filter(User.id == user_id)).scalar()
        return user

