from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from garpix_notify.utils import get_file_path
from garpix_page.models import BasePage
from .tag import Tag


class PostPage(BasePage):
    content = RichTextUploadingField(verbose_name='Содержание', blank=True, default='')
    description = models.CharField(verbose_name='Описание', blank=True, default='', max_length=255)
    image = models.ImageField(upload_to=get_file_path, verbose_name='Изображение', blank=True)
    tags = models.ManyToManyField(Tag, )

    template = "pages/post.html"

    def get_serializer(self):
        from ..serializers import BlogPageSerializer
        return BlogPageSerializer

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ("-created_at",)
