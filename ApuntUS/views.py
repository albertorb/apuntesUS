__author__ = 'AlbertoRinconBorreguero'

from ApuntUS.models import *
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from ApuntUS.forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

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


def apunte(request):
    if request.method == 'POST':
        formulario = ApunteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/apuntus')
    else:
        formulario = ApunteForm()

        return render_to_response('defaultform.html', {'formulario': formulario},
                                  context_instance=RequestContext(request))


def leaving(request, id_apunte):
    apun = get_object_or_404(Apunte, pk=id_apunte)
    punt = get_object_or_404(Puntuacion, apunte=apun.id)
    old = punt.puntos
    new = old + 1
    punt.puntos = new
    punt.save()
    return HttpResponseRedirect(apun.enlace)
