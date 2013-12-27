__author__ = 'AlbertoRinconBorreguero'

from django.contrib import admin
from ApuntUS.models import *

#Registro de modelos
admin.site.register(Apunte)
admin.site.register(Asignatura)
admin.site.register(Puntuacion)
