from flask_wtf          import FlaskForm
from flask_wtf.file     import FileField, FileRequired
from wtforms            import StringField, TextAreaField, SubmitField, PasswordField, IntegerField
from wtforms.validators import InputRequired, Email, DataRequired, Length

class LoginForm(FlaskForm):
	username = StringField(u'Username', validators=[DataRequired(message='Parola sau nume de utilizator incorecte.')])
	password = PasswordField(u'Password', validators=[DataRequired(message='Parola sau nume de utilizator incorecte.')])

class RegisterForm(FlaskForm):
	name = StringField(u'Name', validators=[DataRequired()])
	lastn = StringField(u'Lastn', validators=[DataRequired()])
	username = StringField(u'Username', validators=[DataRequired(message='Enter a unique username.')])
	email = StringField(u'Email', validators=[DataRequired(), Email(message='Enter a valid email.')])
	password = PasswordField(u'Password', validators=[DataRequired(), Length(min=6, message='Select a stronger password.')])

class ServerForm(FlaskForm):
	name_serv = StringField(u'name_serv', validators=[DataRequired()])
	ip_serv = StringField(u'ip_serv', validators=[DataRequired()])
	port_serv = StringField(u'port_serv', validators=[DataRequired()])
	username_fk = StringField(u'username_fk', validators=[DataRequired()])
	

