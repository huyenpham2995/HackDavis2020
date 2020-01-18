from flask_wtf import Flaskform
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


# Python classes representing our forms that will automatically be
# converted into HTML forms within template

# sign up form
# validators to restrict username
class RegistrationForm(Flaskform):
    username = StringField('Username',
                            validators=[DataRequired(Length(min=2, max=20))])
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                            validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                            validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')


class LoginForm(Flaskform):
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                            validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')
