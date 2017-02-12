from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Photo
from .forms import PhotoForm


def hello(request):
    return HttpResponse("안녕하세요!")


def detail(request, pk, hidden=False):
    try:
        photo = Photo.object.get(pk=pk)
    except Photo.DoesNotExist:
        return HttpResponse("사진이 없습니다.")

    if hidden is True:
        # TODO: 은밀한 작업
        pass

    messages = (
        '<p>{pk}번 사진 보여줄게요</p>'.format(pk=photo.pk),
        '<p>주소는 {url}</p>'.format(url=photo.image.url),
    )
    return HttpResponse('\n'.join(messages))


def create(request):
    if request.method == "GET":
        form = PhotoForm()
    elif request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
            return redirect(obj)

    ctx = {
        'form': form,
    }

    return render(request, 'edit.html', ctx)
