from app.forms.extensions import *


class AddMessage(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    name = StringField('Name', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=20, max=500,
                                                                          message="Text must be between 10 and 500 "
                                                                                  "characters")
                                                   ])
    submit = SubmitField('Submit')

