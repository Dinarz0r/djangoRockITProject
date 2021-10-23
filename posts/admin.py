from django.contrib import admin

from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_at'
    list_display = ('id', 'name', 'hash', 'published_at', 'status')
    list_search = ('name',)
