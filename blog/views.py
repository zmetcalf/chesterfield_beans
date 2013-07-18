from django.shortcuts import render, get_object_or_404
from django.template import Context
from blog import blog_entry

def show_blogroll(request, blog_id):
    # TODO set blog_id to human readable
    blogroll = blog_entry.get_blogroll(blog_id)
    title = blog_entry.get_blog_info_title(blog_id)
    sidebar = blog_entry.get_recent(5)
    site_info = {'site_mode': 'blog', 'sidebar': 'left'}
    to_view = Context(dict(list(title.items()) + list(blogroll.items()) + list(site_info.items()) +
                        list(sidebar.items())))
    return render(request, 'blog/blogroll.html', to_view)
    
def show_blog_entry(request, entry_id):
    entry = blog_entry.get_one_entry(entry_id)
    sidebar = blog_entry.get_recent(5)
    site_info = {'site_mode': 'blog', 'sidebar': 'left'}
    to_view = Context(dict(list(entry.items()) + list(site_info.items()) +
                        list(sidebar.items())))
    return render(request, 'blog/entry.html', to_view)