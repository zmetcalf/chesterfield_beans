from django.shortcuts import get_object_or_404

from blog.models import BlogInfo, BlogEntry
    
def get_blog_info_title(slug):
    title = get_object_or_404(BlogInfo, url_slug = slug).title
    return {'title': title}
    
def get_recent(entries):
    bloglist = BlogEntry.objects.all().order_by("-entry_post_date")[:entries]
    return {'bloglist': bloglist}