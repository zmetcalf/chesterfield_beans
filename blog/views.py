from django.shortcuts import render, get_object_or_404
from django.template import Context, RequestContext

from blog import blog_entry
from blog.models import BlogInfo, BlogEntry

def show_blogroll(request, slug):
    blog = get_object_or_404(BlogInfo, url_slug = slug)
    blogroll = blog.blogentry_set.all().order_by("-entry_post_date")[:10]
    title = blog_entry.get_blog_info_title(slug)
    site_info = {'sidebar': 'left', 'blogroll': blogroll}
    to_view = Context(dict(list(title.items()) + list(site_info.items())))
    return render(request, 'blog/blogroll.html', to_view, context_instance = 
                    RequestContext(request, processors=[context_processors]))
    
def show_blog_entry(request, entry_id):
    entry = get_object_or_404(BlogEntry, pk = entry_id)
    site_info = {'sidebar': 'left', 'entry': entry}
    return render(request, 'blog/entry.html', site_info, context_instance = 
                    RequestContext(request, processors=[context_processors]))
    
def context_processors(request):
    return {
        'site_mode': 'blog'
    }