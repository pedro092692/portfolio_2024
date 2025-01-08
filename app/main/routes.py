from flask import render_template, redirect, flash, abort
from app.models.works import Work
from app.models.message import Message
from app.forms.add_message import AddMessage
from app.main import bp


@bp.route('/', methods=['GET', 'POST'])
def home():
    works = Work.get_works()
    form = AddMessage()

    # add new message
    if form.validate_on_submit():
        # message data
        name = form.name.data
        email = form.email.data
        subject = form.subject.data
        message = form.message.data

        # add new message
        new_message = Message.add_message(email, name, subject, message)
        if new_message:
            flash('Message sent I will contact you as soon as possible.')

    return render_template('main/index.html', works=works, form=form)


@bp.route('/project/<slug>', methods=['GET'])
def project(slug):
    work = Work.check_slug(slug)
    if not work:
        return abort(404)

    return render_template('main/project.html', project=work)
