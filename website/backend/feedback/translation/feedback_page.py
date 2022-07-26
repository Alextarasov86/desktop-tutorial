from modeltranslation.translator import TranslationOptions, register
from ..models import FeedbackPage


@register(FeedbackPage)
class FeedbackPageTranslationOptions(TranslationOptions):
    pass
