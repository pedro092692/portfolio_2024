from flask import render_template
from app.security import bp


@bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('security/login.html')

