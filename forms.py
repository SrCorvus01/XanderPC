from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
import re

def institucional_validator(form, field):
    email = field.data or ""
    # ejemplo: dominio institucional @usc.edu.co
    if not re.match(r"^[^@]+@usc\.edu\.co$", email):
        raise ValidationError("Debes usar tu correo institucional @usc.edu.co")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email(), institucional_validator])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField("Confirmar Password", validators=[DataRequired(), EqualTo('password')])

    name = StringField("Nombre", validators=[DataRequired()])
    submit = SubmitField("Registrarse")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Entrar")

class TripForm(FlaskForm):
    origin = StringField("Origen", validators=[DataRequired()])
    destination = StringField("Destino", validators=[DataRequired()])
    departure_time = DateTimeField(
        "Fecha y hora de salida (YYYY-MM-DD HH:MM)", 
        format="%Y-%m-%d %H:%M", 
        validators=[DataRequired()]
    )
    seats = IntegerField("Cupos", validators=[DataRequired()])
    submit = SubmitField("Crear viaje")

class ReportForm(FlaskForm):
    reason = TextAreaField("Motivo", validators=[DataRequired(), Length(min=10)])
    submit = SubmitField("Reportar")

class RatingForm(FlaskForm):
    stars = IntegerField("Estrellas (1-5)", validators=[DataRequired()])
    comment = TextAreaField("Comentario")
    submit = SubmitField("Enviar calificación")
