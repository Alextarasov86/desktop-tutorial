from django.contrib import admin

from ..models.tag import Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass