from django.conf.urls import url, include

from mirror import views

app_name = 'mirror'
urlpatterns = [
    url(r'^season/(?P<seasonNum>[0-9]+)/series/(?P<seriesNum>[0-9]+)/v-originale',
        views.watchEngl, name='watchEngl'),
    url(r'^season/(?P<seasonNum>[0-9]+)/series/(?P<seriesNum>[0-9]+)',
        views.watch, name='watch'),
    url(r'^callback$', views.callback, name='callback'),
    url(r'^subscribe$', views.subscribe, name='subscribe'),
    url(r'^season-(?P<num>[0-9]+)$', views.seasonView, name='season'),
    url(r'^$', views.index, name='index'),
]
