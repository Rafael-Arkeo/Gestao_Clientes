from django.db import models
from django.db.models.fields.files import ImageFieldFile

class Documento(models.Model):
    numero_de_documento = models.CharField(max_length=50)

    def __str__(self):
        return self.numero_de_documento

class Person(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    age = models.IntegerField()
    bio = models.TextField()
    photo = models.ImageField(upload_to='cliente_photos', blank=True, null=True)
    doc = models.OneToOneField(Documento, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name + ' ' + self.last_name
