from app.forms.extensions import *


class AddWork(FlaskForm):
    title = StringField('Work Title', validators=[DataRequired()])
    subtitle = StringField('Work Subtitle', validators=[DataRequired()])
    technology = StringField('Work Used Technology', validators=[DataRequired()])
    image_url = StringField('Work Image URL', validators=[DataRequired(), URL()],
                            render_kw={'placeholder': 'Image URL'})
    summary = StringField('Word Summary', validators=[DataRequired()])
    submit = SubmitField('Upload Work')
