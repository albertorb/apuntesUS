__author__ = 'AlbertoRinconBorreguero'

from django.db import models

#Declaración de los modelos de la aplicación

class asignatura(models.Model):
    nombre = models.TextField()

    def __unicode__(self):
        return self.nombre


class apuntes(models.Model):
    nombre = models.TextField(verbose_name='nombre')
    descripcion = models.TextField(verbose_name='descripción')
    enlace = models.URLField(verbose_name='enlace')
    asig = models.OneToOneField(asignatura, verbose_name='Asignatura')

    def __unicode__(self):
        return self.nombre + ' (' + self.asig.nombre + ')'


class puntuacion(models.Model):
    apunte = models.OneToOneField(apuntes)
    puntos = models.IntegerField()

    def __unicode__(self):
        return self.puntos