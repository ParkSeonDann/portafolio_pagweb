# FORMULARIO USUARIO
from django.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioRegistro(UserCreationForm):
    def __init__(self, *args,**kargs):
        super().__init__(*args,**kargs)
        self.fields['password1'].widget.attrs = { 'class': 'form-control'}
        self.fields['password2'].widget.attrs = { 'class': 'form-control'}
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'first_name',
            'email'
        ]

        widgets = {
            'username': TextInput( attrs = { 'class' : 'form-control'} ),
            'first_name': TextInput( attrs = { 'class' : 'form-control'} ),
            'email': EmailInput( attrs = { 'class' : 'form-control'} ),
        }

class FormularioEntrar(Form):
    usuario = CharField(
        min_length=1,
        max_length=18,
        required = True,
        label = 'Ingrese su usuario',
        widget = TextInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Password'
            }
        )
    )
    contrasenia = CharField(
        required = True,
        min_length = 4,
        max_length = 16,
        label = 'Ingrese su contraseña',
        widget = PasswordInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Password'
            }
        )
    )
    recuerdame = BooleanField(
        required = False,
        label = 'Recordarme',
        widget = CheckboxInput(

        )
    )