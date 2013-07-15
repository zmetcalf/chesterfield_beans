from django.shortcuts import render, get_object_or_404
from django.template import Context, RequestContext

from blog import blog_entry
from cms import cms_content
from site_management.models import SiteVariable

def show_cms(request, content_id):
    content = cms_content.get_content(content_id)
    site_title = get_object_or_404(SiteVariable, option_name__exact='Site Name')
    site_slogan = get_object_or_404(SiteVariable, option_name__exact='Site Slogan')
    sidebar = cms_content.get_recent()
    site_info = {'site_title': site_title, 'site_slogan': site_slogan,
                    'site_mode': 'cms', 'sidebar': 'left'}
    to_view =  Context(dict(list(content.items()) + list(site_info.items() + 
                            list(sidebar.items()))))
    return render(request, 'cms/content.html', to_view)
    
def show_blogroll(request, blog_id):
    # TODO set blog_id to human readable
    blogroll = blog_entry.get_blogroll(blog_id)
    site_title = get_object_or_404(SiteVariable, option_name__exact='Site Name')
    site_slogan = get_object_or_404(SiteVariable, option_name__exact='Site Slogan')
    sidebar = cms_content.get_recent()
    site_info = {'site_title': site_title, 'site_slogan': site_slogan,
                    'site_mode': 'blog', 'sidebar': 'left'}
    to_view = Context(dict(list(blogroll.items()) + list(site_info.items()) +
                        list(sidebar.items())))
    
    return render(request, 'blog/blog.html', to_view)
    
def title_context(request):
    site_title = get_object_or_404(SiteVariable, option_name__exact='Site Name')
    site_slogan = get_object_or_404(SiteVariable, option_name__exact='Site Slogan')
    return {'site_title': site_title, 'site_slogan': site_slogan}