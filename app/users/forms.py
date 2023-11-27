from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
<<<<<<< HEAD:app/forms.py
from .models import User
=======
from flask_login import current_user
>>>>>>> 8e84feb8a342ff6b3978398db18d7f99f90ae38a:app/users/forms.py


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

        
    # create a function for username validation
    def validate_username(self, username):
<<<<<<< HEAD:app/forms.py
        user = User.query.filter_by(username=username.data).first()
        if username.data == user:
=======
        from app.models import User
        # if username.data != current_user.username:
        user = User.query.filter_by(username=username.data).first()
        if user:
>>>>>>> 8e84feb8a342ff6b3978398db18d7f99f90ae38a:app/users/forms.py
            raise ValidationError('That username is taken. Please choose another username')
        
    # create a function for email validation
    def validate_email(self, email):
<<<<<<< HEAD:app/forms.py
        useremail = User.query.filter_by(email=email.data).first()
        if email.data == useremail:
=======
        from app.models import User
        # if email.data != current_user.email:
        user = User.query.filter_by(email=email.data).first()
        if user:
>>>>>>> 8e84feb8a342ff6b3978398db18d7f99f90ae38a:app/users/forms.py
            raise ValidationError('That email is taken. Please choose another email')
    
class loginForm(FlaskForm):    
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

        
    # create a function for username validation
    def validate_username(self, username):
<<<<<<< HEAD:app/forms.py
        user = User.query.filter_by(username=username.data).first()
=======
        from app.models import User
>>>>>>> 8e84feb8a342ff6b3978398db18d7f99f90ae38a:app/users/forms.py
        if username.data != current_user.username:
            
            if user:
                raise ValidationError('That username is taken. Please choose another username')
        
        
    # create a function for email validation
    def validate_email(self, email):
        from app.models import User
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose another email')