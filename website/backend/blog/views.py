from rest_framework import viewsets
from .models import PostPage
from .serializers import BlogTitleSerializer

class BlogPageView(viewsets.ModelViewSet):
    queryset = PostPage.objects.all()
    serializer_class = BlogTitleSerializer