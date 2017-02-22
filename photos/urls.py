from django.conf.urls import url

from . import views

app_name = 'photos'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^hidden-photos/(?P<pk>[0-9]+)$', views.detail, kwargs={'hidden': True}),
    url(r'^upload/$', views.create, name='create'),
    url(r'^new/$', views.photo_new, name='new'),
]
