from django.urls import include, path
from rest_framework.routers import DefaultRouter

from posts.views import PostViewSet

app_name = 'posts'
router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')

urlpatterns = []

urlpatterns += path('', include(router.urls)),
