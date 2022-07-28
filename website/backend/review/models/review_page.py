from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from garpix_page.models import BasePage


class ReviewPage(BasePage):
    comment = RichTextUploadingField(verbose_name='Комментарий', blank=True, default='')
    email = models.EmailField()

    template = "pages/review.html"

    def get_context(self, request=None, *args, **kwargs):
        from ..forms.feedback_form import FeedbackForm
        context = super().get_context(request, *args, **kwargs)
        if request.method == 'POST':
            form = FeedbackForm(request.POST)
            if form.is_valid():
                form.save()
                context.update({
                    'message': 'Спасибо, ваше мнение будет учтено'
                })
            context.update({
                'form': form
            })
        return context

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ("-created_at",)
