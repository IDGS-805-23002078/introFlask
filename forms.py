from wtforms import Form
from wtforms import IntegerField, StringField, PasswordField
from wtforms import EmailField
from wtforms import validators


class UserForm(Form):
    matricula=IntegerField("Matricula", [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=100, max=1000, message="Ingrese valor valido")
    ])
    nombre=StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4, max=10, message="Ingrese nombre valido")
    ])
    apaterno=StringField("Aaterno", [
        validators.DataRequired(message="El campo es requerido")
    ])
    amaterno=StringField("Amterno", [
        validators.DataRequired(message="El campo es requerido")
    ])
    correo=EmailField('Correo', [
        validators.Email(message="El correo valido")

    ])