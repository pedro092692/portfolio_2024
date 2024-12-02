from app.admin import bp
from flask import render_template


@bp.route('/admin')
def admin():
    return render_template('admin/index.html')

