from django.db import models
from garpix_page.models import BaseListPage


class ReviewListPage(BaseListPage):
    paginate_by = 25
    template = 'pages/review_list.html'

    class Meta:
        verbose_name = "ReviewList"
        verbose_name_plural = "ReviewLists"
        ordering = ('-created_at',)
