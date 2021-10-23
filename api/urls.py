from django.urls import include, path

from api.yasg import urlpatterns as doc_urls
from posts import urls as posts_urls

app_name = 'api'

urlpatterns = [
    path('token/', include('djoser.urls.jwt')),
    path('publications/', include(posts_urls)),
]

urlpatterns += doc_urls
