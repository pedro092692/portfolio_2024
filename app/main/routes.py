from flask import render_template, redirect
from app.models.works import Work
from app.main import bp


@bp.route('/', methods=['GET'])
def home():
    works = Work.get_works()
    return render_template('main/index.html', works=works)

