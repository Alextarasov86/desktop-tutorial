from modeltranslation.translator import TranslationOptions, register
from ..models import ReviewListPage


@register(ReviewListPage)
class ReviewListPageTranslationOptions(TranslationOptions):
    pass
