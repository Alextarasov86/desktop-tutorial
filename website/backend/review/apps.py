from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ReviewConfig(AppConfig):
    name = 'review'
    verbose_name = _('Review')
