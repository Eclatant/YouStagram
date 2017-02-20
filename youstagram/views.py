from django.shortcuts import render

from photos.models import Photo


def index(request):
    photo_list = Photo.objects.all().order_by('-created_at')
    ctx = {
        'photo_list': photo_list
    }
    return render(request, 'index.html', ctx)
