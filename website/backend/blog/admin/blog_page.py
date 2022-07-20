from ..models.blog_page import BlogPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(BlogPage)
class BlogPageAdmin(BasePageAdmin):
    pass
