from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from garpix_page.models import BasePage
from garpix_utils.file.file_field import get_file_path




class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class PostPage(BasePage):
    content = RichTextUploadingField(verbose_name='Содержание', blank=True, default='')
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
