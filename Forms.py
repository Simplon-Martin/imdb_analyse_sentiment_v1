from wtforms import Form, BooleanField, StringField, PasswordField, validators
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, ValidationError


class ReviewForm(FlaskForm):
    # email = StringField('Email', validators=[DataRequired(), Email()])
    # password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=8)])
    sentence = TextAreaField('Your Review', validators=[DataRequired()])

    submit = SubmitField("Predict")


    def validate_email(self, email):
        if email.data == 'root@domaine.com':
            raise ValidationError('Cet email est déjà enregisteré !')