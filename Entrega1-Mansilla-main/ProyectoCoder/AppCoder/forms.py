from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AlumnoFormulario(forms.Form):
    nombreAlumno = forms.CharField(max_length = 40)
    apellidoAlumno = forms.CharField(max_length = 40)
    edadAlumno = forms.IntegerField()


class ProfesorFormulario(forms.Form):
    nombreProf = forms.CharField(max_length = 40)
    apellidoProf = forms.CharField(max_length = 40)
    aniosEjerciendo = forms.IntegerField()

class MateriaFormulario(forms.Form):
    nombreMateria = forms.CharField(max_length = 40)
    obligatoria = forms.BooleanField()


class UserRegisterForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
    last_name = forms.CharField(label='Apellido')
    first_name = forms.CharField(label='Nombre')
    

    #imagen_avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name'] 
 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2'] 
        #Saca los mensajes de ayuda
        #help_texts = {k:"" for k in fields}


class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)