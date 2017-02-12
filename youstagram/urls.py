from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

from photos.views import hello
from photos.views import detail
from photos.views import create

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'^hello/$', hello),
    url(r'^photos/(?P<pk>[0-9]+)/$', detail, name='detail'),
    url(r'^hidden-photos/(?P<pk>[0-9]+)$', detail, kwargs={'hidden': True}),
    url(r'^photos/upload/$', create, name='create'),
]

urlpatterns += static('upload_files', document_root=settings.MEDIA_ROOT)
