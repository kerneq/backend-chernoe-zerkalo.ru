from django.conf.urls import url, include

from mirror import views

app_name = 'mirror'
urlpatterns = [
    url(r'^season-(?P<num>[0-9]+)$', views.seasonView, name='season'),
    url(r'^$', views.index, name='index'),
]
