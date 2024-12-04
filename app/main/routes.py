from flask import render_template, redirect
from app.main import bp


@bp.route('/', methods=['GET'])
def home():
    return render_template('main/index.html')

