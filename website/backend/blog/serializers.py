from .models import *
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

class BlogPageSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = PostPage
        fields = '__all__'

class BlogTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostPage
        fields = ('title', )