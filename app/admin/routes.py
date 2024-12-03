from app.admin import bp
from flask import render_template, redirect, url_for
from app.models.works import Work
# forms
from app.forms.add_work import AddWork


@bp.route('/')
def index():
    return render_template('admin/index.html')


@bp.route('/works')
def works():
    return render_template('admin/work/index.html')


@bp.route('/work/add', methods=['GET', 'POST'])
def add_work():
    form = AddWork()

    if form.validate_on_submit():
        title = form.title.data
        subtitle = form.subtitle.data
        technology = form.technology.data
        img_url = form.image_url.data
        summary = form.summary.data

        Work.add_work(title, subtitle, technology, img_url, summary)

        return redirect(url_for('admin.works'))

    return render_template('admin/work/add.html', form=form)


