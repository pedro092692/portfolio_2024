from flask import render_template, redirect
from app.models.works import Work
from app.forms.add_message import AddMessage
from app.main import bp


@bp.route('/', methods=['GET'])
def home():
    works = Work.get_works()
    form = AddMessage()
    return render_template('main/index.html', works=works, form=form)

