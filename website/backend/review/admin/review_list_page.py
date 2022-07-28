from ..models.review_list_page import ReviewListPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(ReviewListPage)
class ReviewListPageAdmin(BasePageAdmin):
    pass
