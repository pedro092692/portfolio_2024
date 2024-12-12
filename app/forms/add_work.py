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
    work_category = StringField('Work category', validators=[DataRequired()])
    full_with = SelectField('Full width for this work ?', choices=[('0', 'False'), ('1', 'True')])
    screenshot_1 = StringField('Screenshot 1', render_kw={'placeholder': 'Screenshot URL'})
    screenshot_2 = StringField('Screenshot 2', render_kw={'placeholder': 'Screenshot URL'})
    screenshot_3 = StringField('Screenshot 3', render_kw={'placeholder': 'Screenshot URL'})
    submit = SubmitField('Upload Work')
