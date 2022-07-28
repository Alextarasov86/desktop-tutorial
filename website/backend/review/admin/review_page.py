from ..models.review_page import ReviewPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(ReviewPage)
class ReviewPageAdmin(BasePageAdmin):
    pass
