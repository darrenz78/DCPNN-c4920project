from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, DecimalField, RadioField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, optional, length
from models import User
from database import DB
import re
from flask import flash

class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired()]) # cant submit empty field
    password = PasswordField('Password', validators=[DataRequired()]) # cant submit empty field
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    firstname = StringField('First name', validators=[DataRequired()])
    lastname = StringField('Last name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    goal = TextAreaField('Your Fitness Goal', validators=[DataRequired(), length(max=200)])
    fitness = RadioField('Fitness Level', choices=[('Beginner','Beginner'),('Intermediate','Intermediate'),('Advanced','Advanced')], coerce=str)#choices=['Low', 'Medium', 'High'], coerce=str)
    weight = DecimalField('Weight', places=2, rounding=None, use_locale=False, number_format=None, validators=[DataRequired()])
    goalweight = DecimalField('Goal Weight', places=2, rounding=None, use_locale=False, number_format=None, validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = DB.find_one("users", {"username": str(username)})
        if user is not None:
            flash('Please use a different username.')
        #if(re.search('^[\W]+$', str(username))):
            #raise ValidationError('Invalid characters. Please use alphanumeric')

    def validate_email(self, email):
        user = DB.find_one("users", {"email": str(email)})
        if user is not None:
            flash('Please use a different email address.')

class EditWeight(FlaskForm):
    weight = DecimalField('Weight', places=2, rounding=None, use_locale=False, number_format=None, validators=[DataRequired()])
    submit = SubmitField('Submit')

class EditGoalWeight(FlaskForm):
    goalweight = DecimalField('Goal Weight', places=2, rounding=None, use_locale=False, number_format=None, validators=[DataRequired()])
    submit = SubmitField('Submit')

class EditGoal(FlaskForm):
    goal = TextAreaField('Your Fitness Goal', validators=[DataRequired(), length(max=200)])
    submit = SubmitField('Submit')

class EditFitness(FlaskForm):
    fitness = RadioField('Fitness Level', choices=[('Beginner','Beginner'),('Intermediate','Intermediate'),('Advanced','Advanced')], coerce=str)
    submit = SubmitField('Submit')

class EditPassword(FlaskForm):
    old_password = PasswordField('Old Password', validators=[DataRequired()])
    password = PasswordField('New Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')



