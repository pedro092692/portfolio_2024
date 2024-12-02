from flask_login import UserMixin, login_required, login_user, logout_user, LoginManager, current_user
from flask_bootstrap import Bootstrap5

login_manager = LoginManager()
login_manager.login_view = "security.login"

