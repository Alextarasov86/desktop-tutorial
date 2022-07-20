from modeltranslation.translator import TranslationOptions, register
from ..models import BlogPage


@register(BlogPage)
class BlogPageTranslationOptions(TranslationOptions):
    pass
