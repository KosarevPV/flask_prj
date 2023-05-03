from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators


class CreatePostForm(FlaskForm):
    title = StringField(
        "Title",
        [validators.DataRequired(0)],
    )
    body = TextAreaField(
        "Body",
        [validators.DataRequired(0)],
    )
    submit = SubmitField("Publish")