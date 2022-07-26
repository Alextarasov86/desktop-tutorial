from django.db import models

from garpix_notify.utils import get_file_path

from solo.models import SingletonModel

class Globals(SingletonModel):
    logo = models.ImageField(upload_to=get_file_path, verbose_name='Логотип', blank=True)
    privacy_policy = models.FileField(upload_to=get_file_path, verbose_name='Политика конфиденциальности', blank=True)

    def __str__(self):
        return "Настройки сайта"

    class Meta:
        verbose_name = "Настройки"
        verbose_name_plural = "Настройки"
