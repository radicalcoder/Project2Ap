from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField, SubmitField, SelectField, TextAreaField
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
     startLocation = SelectField('Start Location',choices= [('DEL', 'New Delhi'), ('BOM','Mumbai'), ('HYD','Hyderabad'), ('GOA','GOA'),('BLR','Bangalore'),])
     endLocation = SelectField('End Location',choices= [('DEL', 'New Delhi'), ('BOM','Mumbai'), ('HYD','Hyderabad'), ('GOA','GOA'),('BLR','Bangalore'),])
     passenger = SelectField('Passenger',choices= [('Adult', 'Adult'), ('Children', 'Children')])
     flightClass = SelectField('Class',choices= [('Business', 'Business'), ('Economy', 'Economy')])
     trip = SelectField('Trip',choices= [('One way', 'One way'), ('Round Trip', 'Round Trip')])
     startDate = IntegerField('Start Date', validators=[DataRequired()])
     endDate = IntegerField('End Date', validators=[DataRequired()])
     submit = SubmitField("Book flight now")

class HotelForm(FlaskForm):
     city = SelectField('Location',choices= [('DEL', 'New Delhi'), ('BOM','Mumbai'), ('HYD','Hyderabad'), ('GOA','GOA'),('BLR','Bangalore'),])
     checkin_date = IntegerField('Check in Date', validators=[DataRequired()])
     checkout_date = IntegerField('Check out Date', validators=[DataRequired()])
     rooms = SelectField('Rooms',choices= [('1 Room 2 Adults', 'One Room'), ('2 Rooms 4 Adults', 'Two Rooms')])
     submit = SubmitField("Book hotel now")
