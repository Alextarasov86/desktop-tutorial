from django.forms import ModelForm
from ..models import FeedbackPage

class FeedbackForm(ModelForm):
    class Meta:
        model = FeedbackPage
        fields = ['email', 'comment']