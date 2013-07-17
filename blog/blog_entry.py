from django.shortcuts import get_object_or_404

from blog.models import BlogInfo, BlogEntry

def get_blogroll(blog_id):
    blog = get_object_or_404(BlogInfo, pk = blog_id)
    blogroll = blog.blogentry_set.all().order_by("-entry_post_date")[:10]
    
    return {'blogroll': blogroll}