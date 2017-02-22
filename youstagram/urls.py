from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('social_django.urls', namespace='social')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^photos/', include('photos.urls', namespace='photos')),
    url(r'^counter/', include('counter.urls', namespace='counter')),
    url(r'^users/', include('profiles.urls')),
    url(r'^$', views.index, name='index'),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
