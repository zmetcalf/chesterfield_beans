from django.shortcuts import render, get_object_or_404
from django.template import Context, RequestContext

from cms.models import Content
    
def get_page(request, slug):
    content = get_object_or_404(Content, url_slug = slug)
    return render(request, 'cms/content.html', {'content': content}, context_instance = 
                    RequestContext(request, processors=[context_processors]))
                    
def context_processors(request):
    return {
        'site_mode': 'cms'
    }
    
def get_home(request):
    return get_page(request, 'home')