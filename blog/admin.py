from django.contrib import admin
from django.utils import timezone

from blog.models import BlogInfo, BlogEntry

class BlogInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'tagline')

class BlogEntryAdmin(admin.ModelAdmin):
    list_display = ('entry_title', 'entry_post_date')
    
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        if getattr(obj, 'entry_post_date', None) is None:
            obj.entry_post_date = timezone.now()
        # TODO add auto-meta/seo maker
        obj.save()
        
admin.site.register(BlogInfo, BlogInfoAdmin)
admin.site.register(BlogEntry, BlogEntryAdmin)