from flask import Blueprint

# declare bp

bp = Blueprint('main', __name__)

# import routes
from app.main import routes






