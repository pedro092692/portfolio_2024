from flask import render_template
from app.security import bp
from app.forms.login import LoginForm


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('security/login.html', form=form)

