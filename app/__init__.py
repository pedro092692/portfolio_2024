from flask import Flask, render_template
from config import Config
from app.extensions import Bootstrap4
from app.extensions import db
from app.extensions import Migrate
from app.extensions import login_manager
from app.extensions import CSRFProtect
from app.database import DataBase
from app.models.user import User


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # database
    app_db = DataBase(db, app)
    app_db.create_tables()
    Migrate(app, db)

    # login manager
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_used(user_id):
        return User.get_user_id(user_id)

    # CSFR
    CSRFProtect(app)

    # plugins
    bootstrap = Bootstrap4(app)

    # blueprints
    from app.main import bp as main_bp
    from app.security import bp as security_bp
    from app.admin import bp as admin_bp
    # register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(security_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')

    @app.errorhandler(404)
    def custom_404(error):
        return render_template('main/404.html')

    @app.errorhandler(400)
    def custom_400(error):
        return render_template('main/400.html')

    if __name__ == "__main__":
        app.run()


create_app()

