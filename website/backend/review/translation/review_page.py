from modeltranslation.translator import TranslationOptions, register
from ..models import ReviewPage


@register(ReviewPage)
class ReviewPageTranslationOptions(TranslationOptions):
    pass
