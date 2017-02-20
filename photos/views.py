from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .forms import PhotoForm
from .models import Photo


def photo_new(request):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            # photo.user = request.user
            # photo.image = form.
            # photo.save()
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('detail', pk=f.id)
        return HttpResponse("Hell world")
    else:
        form = PhotoForm()
        return render(request, 'photos/edit.html', {'form': form})

def index(request):
    ctx = {}
    return render(request, 'index.html', ctx)


def hello(request):
    return HttpResponse("안녕하세요!")


def detail(request, pk, hidden=False):
    try:
        photo = Photo.objects.get(pk=pk)
    except Photo.DoesNotExist:
        return HttpResponse("사진이 없습니다.")

    if hidden is True:
        pass

    messages = (
        '<p>{pk}번 사진 보여줄게요</p>'.format(pk=photo.pk),
        '<img src={url}>'.format(url=photo.image.url),
        '<p>주소는 {url}</p>'.format(url=photo.image.url),
    )
    return HttpResponse('\n'.join(messages))


@login_required
def create(request):
    if request.method == "GET":
        form = PhotoForm()
    elif request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj = form.save()
            return redirect(obj)

    ctx = {
        'form': form,
    }

    return render(request, 'edit.html', ctx)
