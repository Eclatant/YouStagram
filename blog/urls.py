from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.post_list, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='detail'),
    url(r'^post/new/$', views.post_new, name='new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='edit'),
]
