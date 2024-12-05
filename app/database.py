import os
from app.extensions import generate_password_hash

# app models
from app.models.user import User
from app.models.works import Work
from app.models.screenshots import ScreenShot
from app.models.message import Message


class DataBase:
    def __init__(self, db, app):
        self.db = db
        self.app = app

        # initialization db
        self.db.init_app(self.app)

    def create_tables(self):
        with self.app.app_context():
            self.db.create_all()
            # check if admin user exist
            if not User.get_user_id(user_id=1):
                User.create_user(
                    os.environ.get('ADMIN_USER_EMAIL'),
                    generate_password_hash(
                        password=os.environ.get('ADMIN_PASSWORD'), method='pbkdf2:sha256', salt_length=8
                    ),
                    'admin'
                )




