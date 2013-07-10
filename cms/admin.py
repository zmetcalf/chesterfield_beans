from django.contrib import admin
from django.utils import timezone

from cms.models import Content

class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_post_date')
    
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        if getattr(obj, 'content_post_date', None) is None:
            obj.content_post_date = timezone.now()
        # TODO add auto-meta/seo maker
        obj.save()
        
admin.site.register(Content, ContentAdmin)