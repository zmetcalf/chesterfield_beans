from django.shortcuts import get_object_or_404

from blog.models import BlogInfo, BlogEntry

def get_blogroll(blog_id):
    # TODO Insert logic for grabbing certain blog - ie blog_id
    blogroll = BlogEntry.objects.all().order_by("-entry_post_date")[:10]
    return {'blogroll': blogroll}