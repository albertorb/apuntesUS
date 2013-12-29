__author__ = 'AlbertoRinconBorreguero'

from ApuntUS.models import *
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404

# Declaración de las vistas de la aplicación

def main(request):
    asignaturas = Asignatura.objects.all()
    apuntes = []
    for elem in Puntuacion.objects.all().order_by('puntos').reverse():
        if (apuntes.__len__() > 4):
            break
        apuntes.append(elem.apunte)
    return render_to_response('main.html', {'asignaturas': asignaturas, 'apuntes': apuntes})


def apuntes_por_asignatura(request, id_asignatura):
    apuntes = Apunte.objects.all().filter(asig=id_asignatura)
    asignatura = get_object_or_404(Asignatura, pk=id_asignatura)

    return render_to_response('files.html', {'apuntes': apuntes, 'asignatura': asignatura})

