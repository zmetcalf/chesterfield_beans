from django.contrib import admin
from cms.models import Content

class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_post_date')

admin.site.register(Content, ContentAdmin)