import os
from app.extensions import generate_password_hash
from app.models.user import User


class DataBase:
    def __init__(self, db, app):
        self.db = db
        self.app = app

    def create_tables(self):
        with self.app.app_context():
            self.db.create_all()
            # check if admin user exist
            if not User.get_user_id(user_id=1):
                User.create_user(
                    email=os.environ.get('ADMIN_USER_EMAIL'),
                    password=generate_password_hash(password=os.environ.get('ADMIN_PASSWORD'), method='pbkdf2:sha256',
                                                    salt_length=8,
                    role='admin')
                )




