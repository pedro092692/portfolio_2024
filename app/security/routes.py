from flask import render_template
from app.security import bp


@bp.route('/login', methods=['GET', 'POST'])
def login():
    return 'login here'

