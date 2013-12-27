#encoding: utf-8
__author__ = 'AlbertoRinconBorreguero'

from django.db import models

#Declaración de los modelos de la aplicación

class Asignatura(models.Model):
    nombre = models.TextField()

    def __unicode__(self):
        return str(self.nombre)


class Apunte(models.Model):
    nombre = models.TextField(verbose_name='nombre')
    descripcion = models.TextField(verbose_name='descripción')
    enlace = models.URLField(verbose_name='enlace')
    asig = models.OneToOneField(Asignatura, verbose_name='Asignatura')

    def __unicode__(self):
        return self.nombre + ' (' + self.asig.nombre + ')'


class Puntuacion(models.Model):
    apunte = models.ForeignKey(Apunte, unique=True)
    puntos = models.IntegerField()

    def __unicode__(self):
        return str(self.puntos)