from app.admin import bp
from flask import render_template


@bp.route('/')
def index():
    return render_template('admin/index.html')


@bp.route('/works')
def works():
    return render_template('admin/work.html')


