from django.urls import path
from AppCoder import views

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('inicio', views.inicio, name="Inicio"),

    #CRUD
    ##Alumno
    path('listaAlumnos', views.AlumnoList.as_view(), name='ListaAlumnos'),
    path(r'^(?P<pk>\d+)$', views.AlumnoDetail.as_view(), name='Detail'),
    path(r'^nuevo$', views.AlumnoCreate.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.AlumnoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.AlumnoDelete.as_view(), name='Delete'),
    ##Profesor

    path('profesor/list', views.ProfesorList.as_view(), name = 'ProfesorList'),
    path(r'^(?P<pk>\d+)p$', views.ProfesorDetalle.as_view(), name = 'ProfesorDetail'),
    path(r'^nuevoprof$', views.ProfesorCreacion.as_view(), name = 'ProfesorNew'),
    path(r'^editarprof/(?P<pk>\d+)$', views.ProfesorUpdate.as_view(), name = 'ProfesorEdit'),
    path(r'^borrarprof/(?P<pk>\d+)$', views.ProfesorDelete.as_view(), name = 'ProfesorDelete'),

    ##Materia
    path('materia/list', views.MateriaList.as_view(), name = 'MateriaList'),
    path(r'^(?P<pk>\d+)m$', views.MateriaDetalle.as_view(), name = 'MateriaDetail'),
    path(r'^nuevomat$', views.MateriaCreacion.as_view(), name = 'MateriaNew'),
    path(r'^editarmat/(?P<pk>\d+)$', views.MateriaUpdate.as_view(), name = 'MateriaEdit'),
    path(r'^borrarmat/(?P<pk>\d+)$', views.MateriaDelete.as_view(), name = 'MateriaDelete'),
    
    

    #USER
    path('login', views.login_request, name = 'Login'), 
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name = 'Logout'),
    path('register', views.register, name = 'Register'),
    path('editarPerfil', views.editarPerfil, name = 'EditarPerfil'),
    path('agregarAvatar', views.agregarAvatar, name = 'AgregarAvatar')
]