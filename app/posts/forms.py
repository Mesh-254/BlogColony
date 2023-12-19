from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    image = FileField('Image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')
    ])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
