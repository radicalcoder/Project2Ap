from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from FlaskWebProjectAssignment.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class FlightForm(FlaskForm):
     start_Location = SelectField('Start Location',choices= [('DEL', 'New Delhi'), ('BOM','Mumbai'), ('HYD','Hyderabad'), ('GOA','GOA'),('BLR','Bangalore'),])
     end_Location = SelectField('End Location',choices= [('DEL', 'New Delhi'), ('BOM','Mumbai'), ('HYD','Hyderabad'), ('GOA','GOA'),('BLR','Bangalore'),])
     icing = SelectField('Icing',choices= [('bt', 'Buttercream'), ('fc','Fresh Cream'), ('gn','Ganache')])
     decorations = SelectField('Decorations',choices= [('flow', 'Flowers'), ('frt','Fresh Fruits'), ('cc','Crushed Candy')])
     egg = SelectField('Egg', choices =[('e','Egg'), ('eggl','Eggless')])
     
     submit = SubmitField("Order Now")

