from flask import render_template, redirect
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
        Message.add_message(email, name, subject, message)

    return render_template('main/index.html', works=works, form=form)

