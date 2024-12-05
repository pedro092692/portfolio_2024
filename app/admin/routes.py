from app.admin import bp
from flask import render_template, redirect, url_for
from app.models.works import Work
from app.models.message import Message
from app.models.screenshots import ScreenShot
# forms
from app.forms.add_work import AddWork
from app.forms.add_message import AddMessage


@bp.route('/')
def index():
    total_works = len(Work.get_works())
    total_messages = len(Message.get_messages())
    return render_template('admin/index.html', total_works=total_works, total_messages=total_messages)


@bp.route('/works')
def works():
    content = Work.get_works()
    return render_template('admin/work/index.html', works=content)


@bp.route('/work/add', methods=['GET', 'POST'])
def add_work():
    form = AddWork()

    if form.validate_on_submit():
        title = form.title.data
        subtitle = form.subtitle.data
        technology = form.technology.data
        img_url = form.image_url.data
        summary = form.summary.data
        project_url = form.work_url.data
        repository_url = form.work_repository_url.data

        new_work = Work.add_work(title, subtitle, technology, img_url, summary, project_url, repository_url)

        # add screenshots
        screenshots = [form.screenshot_1.data, form.screenshot_2.data, form.screenshot_3.data]

        for screenshot in screenshots:
            if screenshot:
                ScreenShot.add_screenshot(new_work.id, screenshot)

        return redirect(url_for('admin.works'))

    return render_template('admin/work/add.html', form=form)


@bp.route('/work/<id_work>', methods=['GET', 'POST'])
def work(id_work):
    form = AddWork()
    form.submit.label.text = 'Update Work'
    work_item = Work.get_work(id_work)

    # update work
    if form.validate_on_submit():
        title = form.title.data
        subtitle = form.subtitle.data
        technology = form.technology.data
        image_url = form.image_url.data
        summary = form.summary.data
        url = form.work_url.data
        repository_url = form.work_repository_url.data
        f_screens = [form.screenshot_1, form.screenshot_2, form.screenshot_3]

        # update object work
        Work.update_work(work_item, title, subtitle, technology, image_url, summary, url, repository_url)

        # update screenshots
        for i in range(len(work_item.screenshots)):
            if work_item.screenshots[i].img_url != f_screens[i].data:
                if f_screens[i].data == '':
                    # delete screenshot
                    ScreenShot.delete_screenshot(work_item.screenshots[i])
                    return redirect(url_for('admin.works'))
                else:
                    # update
                    ScreenShot.update_screenshot(work_item.screenshots[i], work_item.id, f_screens[i].data)

        # add screenshot if work obj has less than 3
        if len(work_item.screenshots) < 3:
            for i in range(len(f_screens)):
                if f_screens[i].data != '':
                    try:
                        print(work_item.screenshots[i].img_url)
                    except IndexError:
                        # add new screenshot
                        ScreenShot.add_screenshot(work_item.id, f_screens[i].data)

        return redirect(url_for('admin.works'))

    # work info
    form.title.data = work_item.title
    form.subtitle.data = work_item.subtitle
    form.technology.data = work_item.technology
    form.summary.data = work_item.summary
    form.image_url.data = work_item.image_url
    form.work_repository_url.data = work_item.repository_url
    form.work_url.data = work_item.url
    # fill work screenshots
    screenshots = work_item.screenshots
    form_screenshots = [form.screenshot_1, form.screenshot_2, form.screenshot_3]
    for i in range(len(screenshots)):
        form_screenshots[i].data = screenshots[i].img_url

    return render_template('admin/work/work.html', form=form, work=work_item)


@bp.route('/work/delete/<id_work>', methods=['POST'])
def delete_work(id_work):
    work_item = Work.get_work(id_work)
    Work.delete_work(work_item)
    return redirect(url_for('admin.works'))


@bp.route('/messages', methods=['GET'])
def messages():
    content = Message.get_messages(paginate=True)
    return render_template('admin/messages/index.html', messages=content)


@bp.route('/message/<message_id>')
def message_info(message_id):
    message = Message.get_message(message_id)
    form = AddMessage()
    # fill form
    form.email.data = message.email
    form.name.data = message.name
    form.subject.data = message.subject
    form.message.data = message.message

    # set all fields in readonly mode
    for name, field in form._fields.items():
        field.render_kw = {'readonly': True}

    return render_template('admin/messages/message.html', message=message, form=form)


@bp.route('/message/delete/<message_id>', methods=['POST'])
def delete_message(message_id):
    message = Message.get_message(message_id)
    Message.delete_message(message)
    return redirect(url_for('admin.messages'))

