from django.shortcuts import render, get_object_or_404
from django.template import Context

from blog import blog_entry
from blog.models import BlogInfo, BlogEntry

def show_blogroll(request, blog_id):
    # TODO set blog_id to human readable
    blog = get_object_or_404(BlogInfo, pk = blog_id)
    blogroll = blog.blogentry_set.all().order_by("-entry_post_date")[:10]
    title = blog_entry.get_blog_info_title(blog_id)
    sidebar = blog_entry.get_recent(5)
    site_info = {'site_mode': 'blog', 'sidebar': 'left', 'blogroll': blogroll}
    to_view = Context(dict(list(title.items()) + list(site_info.items()) +
                        list(sidebar.items())))
    return render(request, 'blog/blogroll.html', to_view)
    
def show_blog_entry(request, entry_id):
    entry = get_object_or_404(BlogEntry, pk = entry_id)
    sidebar = blog_entry.get_recent(5)
    site_info = {'site_mode': 'blog', 'sidebar': 'left', 'entry': entry}
    to_view = Context(dict(list(site_info.items()) + list(sidebar.items())))
    return render(request, 'blog/entry.html', to_view)