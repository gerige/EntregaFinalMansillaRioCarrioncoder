from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Alumno(models.Model):
    nombreAlumno = models.CharField(max_length = 40)
    apellidoAlumno = models.CharField(max_length = 40)
    edadAlumno = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombreAlumno} - Apellido: {self.apellidoAlumno} - Edad: {self.edadAlumno}"

class Profesor(models.Model):
    nombreProf = models.CharField(max_length = 40)
    apellidoProf = models.CharField(max_length = 40)
    aniosEjerciendo = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombreProf} - Apellido: {self.apellidoProf} - Anios Ejerciendo: {self.aniosEjerciendo}"

class Materia(models.Model):
    nombreMateria = models.CharField(max_length = 40)
    obligatoria = models.BooleanField()

    def __str__(self):
        return f"Nombre: {self.nombreMateria} - Obligatoria: {self.obligatoria}"


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)