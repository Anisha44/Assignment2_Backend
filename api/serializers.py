from rest_framework import serializers

from api.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'category', 'created_at', 'updated_at', 'author']
        read_only_fields = ['id', 'created_at', 'updated_at', 'author']
