from django.shortcuts import render, get_object_or_404
from django.template import Context, RequestContext

from blog import blog_entry
from cms import cms_content
from site_management.models import SiteVariable

def show_cms(request, content_id):
    content = cms_content.get_content(content_id)
    site_title = get_object_or_404(SiteVariable, option_name__exact='Site Name')
    site_slogan = get_object_or_404(SiteVariable, option_name__exact='Site Slogan')
    sidebar = blog_entry.get_recent(5)
    site_info = {'site_title': site_title, 'site_slogan': site_slogan,
                    'site_mode': 'cms', 'sidebar': 'left'}
    to_view =  Context(dict(list(content.items()) + list(site_info.items() + 
                            list(sidebar.items()))))
    return render(request, 'cms/content.html', to_view)
    
def show_blogroll(request, blog_id):
    # TODO set blog_id to human readable
    blogroll = blog_entry.get_blogroll(blog_id)
    title = blog_entry.get_blog_info_title(blog_id)
    site_title = get_object_or_404(SiteVariable, option_name__exact='Site Name')
    site_slogan = get_object_or_404(SiteVariable, option_name__exact='Site Slogan')
    sidebar = blog_entry.get_recent(5)
    site_info = {'site_title': site_title, 'site_slogan': site_slogan,
                    'site_mode': 'blog', 'sidebar': 'left'}
    to_view = Context(dict(list(title.items()) + list(blogroll.items()) + list(site_info.items()) +
                        list(sidebar.items())))
    return render(request, 'blog/blogroll.html', to_view)
    
def show_blog_entry(request, entry_id):
    entry = blog_entry.get_one_entry(entry_id)
    site_title = get_object_or_404(SiteVariable, option_name__exact='Site Name')
    site_slogan = get_object_or_404(SiteVariable, option_name__exact='Site Slogan')
    sidebar = blog_entry.get_recent(5)
    site_info = {'site_title': site_title, 'site_slogan': site_slogan,
                    'site_mode': 'blog', 'sidebar': 'left'}
    to_view = Context(dict(list(entry.items()) + list(site_info.items()) +
                        list(sidebar.items())))
    return render(request, 'blog/entry.html', to_view)
    
def title_context(request):
    site_title = get_object_or_404(SiteVariable, option_name__exact='Site Name')
    site_slogan = get_object_or_404(SiteVariable, option_name__exact='Site Slogan')
    return {'site_title': site_title, 'site_slogan': site_slogan}