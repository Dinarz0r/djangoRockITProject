from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from api.decorators import common_schema_decorator
from posts.models import Post
from posts.serializers import PostSerializer


@common_schema_decorator(tags=['Публикации'])
class PostViewSet(IsAuthenticated, viewsets.ModelViewSet):
    queryset = Post.objects.select_related('author').all()
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ['hash']
    filterset_fields = ['published_at', 'status']
    lookup_url_kwarg = 'hash'
    lookup_field = 'hash'
