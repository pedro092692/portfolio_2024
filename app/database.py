import os
from app.extensions import generate_password_hash


class DataBase:
    def __init__(self, db, app):
        self.db = db
        self.app = app

