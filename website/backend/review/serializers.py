from .models import *
from rest_framework import serializers

class ReviewPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewPage
        fields = ('email', 'comment')