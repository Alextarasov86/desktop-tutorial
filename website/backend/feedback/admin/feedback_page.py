
from ..models.feedback_page import FeedbackPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(FeedbackPage)
class FeedbackPageAdmin(BasePageAdmin):
    pass
