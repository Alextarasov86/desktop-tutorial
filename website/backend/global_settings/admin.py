from django.contrib import admin

from solo.admin import SingletonModelAdmin
from .models import Globals

@admin.register(Globals)
class GlobalAdmin(SingletonModelAdmin):
    pass
