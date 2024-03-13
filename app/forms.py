from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember_me = BooleanField('Remember me')

class UploadForm(FlaskForm):
    photofile = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    