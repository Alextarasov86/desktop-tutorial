from django.forms import ModelForm
from ..models import ReviewPage

class FeedbackForm(ModelForm):
    class Meta:
        model = ReviewPage
        fields = ['email', 'comment']