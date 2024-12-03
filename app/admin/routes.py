from app.admin import bp
from flask import render_template
# forms
from app.forms.add_work import AddWork


@bp.route('/')
def index():
    return render_template('admin/index.html')


@bp.route('/works')
def works():
    form = AddWork()
    return render_template('admin/work/index.html', form=form)


