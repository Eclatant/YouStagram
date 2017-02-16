from django.db import models
from django.core.urlresolvers import reverse_lazy
from django.conf import settings


class Photo(models.Model):
    # id = "개별 사진을 구분하는 색인값"
    # image = "원본 사진 파일"
    # filtered_image = "필터 적용된 사진 파일"
    # content = "사진에 대한 설명문"
    # created_at = "생성일시"

    image = models.ImageField(upload_to='%Y/%m/%d/original')
    filtered_image = models.ImageField(upload_to='%Y/%m/%d/filtered')
    content = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.image.name

    def delete(self, *args, **kwargs):
        self.image.delete()
        self.filtered_image.delete()
        super(Photo, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        url = reverse_lazy('detail', kwargs={'pk': self.pk})
        return url
