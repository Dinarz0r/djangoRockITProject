from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор модели Post"""
    author_name = serializers.CharField(source='author', read_only=True)
    status_name = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['hash']
