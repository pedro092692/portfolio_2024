from flask import Flask
from config import Config
from extensions import Bootstrap5


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    # plugins
    bootstrap = Bootstrap5(app)

    # blueprints
    from app.main import bp as main_bp
    from app.security import bp as security_bp
    # register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(security_bp)

    @app.route('/test')
    def test_route():
        return 'this is a test rute.'

    return app


