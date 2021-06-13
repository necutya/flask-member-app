from flask_wtf import FlaskForm
from wtforms import StringField, validators


class RegistrationForm(FlaskForm):
    name = StringField('Name', [
        validators.DataRequired(),
        validators.Length(min=2, max=25),
        validators.Regexp(r'^[a-zA-Z\s\.]+$', message="Name can contain only English letters, dots and spaces.")
    ])
    email = StringField('Email', [
        validators.DataRequired(),
        validators.Length(min=4, max=35), validators.Email()
    ])
