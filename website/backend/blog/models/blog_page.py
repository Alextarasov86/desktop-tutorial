from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from garpix_page.models import BasePage
from garpix_utils.file.file_field import get_file_path

from .tag import Tag


class BlogPage(BasePage):
    content = RichTextUploadingField(verbose_name='Содержание', blank=True, default='')
    image = models.ImageField(upload_to=get_file_path, verbose_name='Изображение', blank=True)
    tags = models.ManyToManyField(Tag, )

    template = "pages/blog.html"

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ("-created_at",)
