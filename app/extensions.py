from flask_login import UserMixin, login_required, login_user, logout_user, LoginManager, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bootstrap import Bootstrap4
from flask_wtf.csrf import CSRFProtect
from sqlalchemy.orm import Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from typing import List
from flask_migrate import Migrate
from datetime import datetime
from dotenv import load_dotenv
from flask_paginate import Pagination, get_page_parameter
from slugify import slugify

# Configure login manager
login_manager = LoginManager()
login_manager.login_view = "security.login"

# Configure Database
db = SQLAlchemy()

# load dotenv var
load_dotenv()
