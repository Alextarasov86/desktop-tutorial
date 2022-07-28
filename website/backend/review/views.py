from rest_framework import viewsets
from .models import ReviewPage
from .serializers import ReviewPageSerializer


class ReviewPageView(viewsets.ModelViewSet):
    queryset = ReviewPage.objects.all()
    serializer_class = ReviewPageSerializer
