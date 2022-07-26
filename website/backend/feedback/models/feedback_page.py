from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from garpix_page.models import BasePage


class FeedbackPage(BasePage):
    comment = RichTextUploadingField(verbose_name='Комментарий', blank=True, default='')
    email = models.EmailField()
    template = "pages/feedback1.html"

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"
        ordering = ("-created_at",)
