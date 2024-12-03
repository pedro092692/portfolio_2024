from flask import render_template, request, redirect, flash, url_for
from app.extensions import check_password_hash, login_user, logout_user
from app.security import bp
from app.forms.login import LoginForm
from app.models.user import User


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # retrieve form data
        email = form.email.data
        password = form.password.data
        # check if user exist
        user = User.find_user(email)
        if user and check_password_hash(user.password, password):
            # login user
            login_user(user)
            # redirect user
            next_url = request.args.get('next')
            return redirect(next_url or url_for('main.home'))
        else:
            flash('Incorrect Credentials')
    return render_template('security/login.html', form=form)


@bp.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('main.home'))

