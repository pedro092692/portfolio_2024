from flask_login import UserMixin, login_required, login_user, logout_user, LoginManager, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bootstrap import Bootstrap5
from sqlalchemy.orm import Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from flask_migrate import Migrate
from dotenv import load_dotenv

# Configure login manager
login_manager = LoginManager()
login_manager.login_view = "security.login"

# Configure Database
db = SQLAlchemy()

# load dotenv var
load_dotenv()