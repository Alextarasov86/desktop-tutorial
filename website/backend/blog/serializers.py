from rest_framework import serializers

from .models import Tag, BlogPage


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

class BlogPageSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = BlogPage
        fields = "__all__"