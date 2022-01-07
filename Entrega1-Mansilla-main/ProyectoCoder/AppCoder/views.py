from django.db.models import fields
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from AppCoder.models import *
from AppCoder.forms import *

# Create your views here.

def inicio(request):

    diccionario = {}
    cantAvatares = 0

    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(user = request.user.id)

        for a in avatar:
            cantAvatares = cantAvatares + 1

        #Si el usuario tiene mas de 1 avatar cargado mando la url del ultimo, sino mando el diccionario vacio
        if cantAvatares > 0: 
            diccionario["avatar_url"] = avatar[cantAvatares-1].imagen.url

    return render(request, 'AppCoder/inicio.html', diccionario)



####################################################################
##########################ALUMNOS###################################
####################################################################

class AlumnoList(ListView):
    model = Alumno
    template_name = "AppCoder/alumnos_list.html"

class AlumnoDetail(DetailView):
    model = Alumno
    template_name = "AppCoder/alumnos_detail.html"

class AlumnoCreate(CreateView):
      model = Alumno
      template_name = "AppCoder/alumnos_form.html"
      success_url = "/AppCoder/listaAlumnos"
      fields = ["nombreAlumno", "apellidoAlumno", "edadAlumno"]

class AlumnoUpdate(UpdateView):
    model = Alumno
    template_name = "AppCoder/alumnos_form.html"
    success_url = "../listaAlumnos"
    fields = ["nombreAlumno", "apellidoAlumno", "edadAlumno"]

class AlumnoDelete(DeleteView):
    model = Alumno
    template_name = "AppCoder/alumnos_confirm_delete.html"
    success_url = "../listaAlumnos"

####################################################################
##########################PROFESORES################################
####################################################################
class ProfesorList(ListView):

      model = Profesor 
      template_name = "AppCoder/profesor_list.html"


class ProfesorDetalle(DetailView):

      model = Profesor
      template_name = "AppCoder/profesor_detalle.html"



class ProfesorCreacion(CreateView):

      model = Profesor
      success_url = "/AppCoder/profesor/list"
      fields = ['nombreProf', 'apellidoProf', 'aniosEjerciendo']


class ProfesorUpdate(UpdateView):

      model = Profesor
      success_url = "/AppCoder/profesor/list"
      fields  = ['nombreProf', 'apellidoProf', 'aniosEjerciendo']


class ProfesorDelete(DeleteView):

      model = Profesor
      success_url = "/AppCoder/profesor/list"



####################################################################
##########################MATERIAS##################################
####################################################################

class MateriaList(ListView):

          model = Materia
          template_name = "AppCoder/materia_list.html"


class MateriaDetalle(DetailView):

      model = Materia
      template_name = "AppCoder/materia_detalle.html"



class MateriaCreacion(CreateView):

      model = Materia
      success_url = "/AppCoder/materia/list"
      fields = ['nombreMateria', 'obligatoria']


class MateriaUpdate(UpdateView):

      model = Materia
      success_url = "/AppCoder/materia/list"
      fields  = ['nombreMateria', 'obligatoria']


class MateriaDelete(DeleteView):

      model = Materia
      success_url = "/AppCoder/materia/list"


#############LOGIN#############
def login_request(request):

      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username=usuario, password=contra)

                  if user is not None:
                        login(request, user)
                        return render(request,"AppCoder/inicio.html",  {"mensaje":f"Bienvenido {usuario}"} )
                  else:
                        return render(request,"AppCoder/inicio.html", {"mensaje":"Error, datos incorrectos"} )

            else:
                        return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Error, formulario erroneo"})

      form = AuthenticationForm()

      return render(request,"AppCoder/login.html", {'form':form} )

#############Dar de Alta usuarios desde la web#############
def register(request):

      if request.method == 'POST':
            form = UserRegisterForm(request.POST) #UserRegisterForm declarado en forms.py
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":f"Usuario {username} Creado"})


      else:      
            form = UserRegisterForm()     

      return render(request,"AppCoder/register.html" ,  {"form":form})


#############Edicion de usuarios#############
@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST) #UserEditForm declarado en froms.py
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            #No me sirvio hacerlo como en el ppt, no se modificaba el password
            #usuario.email       = informacion['email']
            #usuario.password1   = informacion['password1']
            #usuario.password2   = informacion['password2']
            #usuario.save()

            usuario.email       = informacion['email']
            usuario.set_password(informacion['password1'])
            usuario.save()

            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})

    return render(request, "AppCoder/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})


#############Permitir al usuario cargar imagenes para su avatar#############

@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        miFormulario = AvatarFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():
            u = User.objects.get(username=request.user)

            avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen'])
            avatar.save()

            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = AvatarFormulario()

    return render(request, "AppCoder/agregarAvatar.html", {"miFormulario":miFormulario})