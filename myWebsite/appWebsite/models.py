from django.db import models

# Create your models here.

# Create your models here.
# Los modelos son pequeñas clases que van a generar objetos para trabajar
# dentro del proyecto de Django con las entidades del proyecto
# Los modelos representan las tablas dentro de la base de datos

class Article(models.Model): # La herencia es para decirle a Python que esta clase es un modelo
    title = models.CharField(max_length = 110)
    content = models.TextField()
    public = models.BooleanField()
    image = models.ImageField(default = 'null')
    created_at = models.DateTimeField(auto_now_add=True) # Cuando guardemos un registro nos va a guardar la fecha y hora actual
    updated_at = models.DateTimeField(auto_now=True) # Cuando guardemos un registro nos va a guardar la fecha y hora actual

class Category(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 250)
    created_at = models.DateField()