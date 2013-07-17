from django.shortcuts import get_object_or_404

from blog.models import BlogInfo, BlogEntry

def get_blogroll(blog_id):
    blog = get_object_or_404(BlogInfo, pk = blog_id)
    blogroll = blog.blogentry_set.all().order_by("-entry_post_date")[:10]
    return {'blogroll': blogroll}
    
def get_one_entry(entry_id):
    entry = get_object_or_404(BlogEntry, pk = entry_id)
    return {'entry': entry}
    
def get_blog_info_title(blog_id):
    title = get_object_or_404(BlogInfo, pk = blog_id).title
    return {'title': title}
    
def get_recent(entries):
    bloglist = BlogEntry.objects.all().order_by("-entry_post_date")[:entries]
    return {'bloglist': bloglist}