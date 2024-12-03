from app.forms.extensions import *


class AddWork(FlaskForm):
    title = StringField('Work Title', validators=[DataRequired()])
    subtitle = StringField('Work Subtitle', validators=[DataRequired()])
    technology = StringField('Used Technology', validators=[DataRequired()])
    image_url = StringField('Work Image URL', validators=[DataRequired(), URL()],
                            render_kw={'placeholder': 'Image URL'})
    summary = StringField('Work Summary', validators=[DataRequired()])
    work_url = StringField('Work url', render_kw={'placeholder': 'Project URL'})
    work_repository_url = StringField('Repository url', validators=[DataRequired(), URL()],
                                      render_kw={'placeholder': 'Repository URL'})
    submit = SubmitField('Upload Work')
