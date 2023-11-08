from django.contrib import admin
from .models import Post


class AdminPost(admin.ModelAdmin):
    list_display = ('user', 'body', 'created')
    search_fields = ('body',)
    list_filter = ('slug', 'user',)
    prepopulated_fields = {'slug': ('body', 'user')}
    raw_id_fields = ('user',)


admin.site.register(Post, AdminPost)

