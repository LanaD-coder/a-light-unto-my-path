from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment
from django.utils import timezone


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author', 'status', 'created_on', 'image')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

    # Add scheduled_published_date field
    fieldsets = (
        (None, {
            'fields': (
                'title', 'slug', 'content', 'excerpt', 'status', 'image', 'author', 'scheduled_publish_date')
        }),
        ('Date Information', {
            'fields': ('created_on', 'updated_on')
        }),
 )


# Register your models here.
admin.site.register(Comment)
