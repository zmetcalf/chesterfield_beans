from django.shortcuts import render, get_object_or_404
from django.template import Context, RequestContext

from blog import blog_entry
from cms import cms_content
from cms.models import Content
    
def get_page(request, slug):
    content = get_object_or_404(Content, url_slug = slug)
    sidebar = blog_entry.get_recent(5)
    site_info = {'content': content}
    to_view =  Context(dict(list(site_info.items() + list(sidebar.items()))))
    return render(request, 'cms/content.html', to_view, context_instance = 
                    RequestContext(request, processors=[context_processors]))
                    
def context_processors(request):
    return {
        'site_mode': 'cms'
    }
    
def get_home(request):
    return get_page(request, 'home')