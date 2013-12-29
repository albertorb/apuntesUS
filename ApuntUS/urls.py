from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ApuntUS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^apuntus/', 'ApuntUS.views.main'),
    url(r'^files/(?P<id_asignatura>\d+)$', 'ApuntUS.views.apuntes_por_asignatura'),
    url(r'^aporteform/', 'ApuntUS.views.apunte'),
    url(r'^leaving/(?P<id_apunte>\d+)$', 'ApuntUS.views.leaving'),
)
