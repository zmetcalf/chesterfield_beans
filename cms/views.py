from django.shortcuts import render, get_object_or_404
from django.template import Context

from cms import cms_content
from blog import blog_entry

def show_cms(request, content_id):
    content = cms_content.get_content(content_id)
    sidebar = blog_entry.get_recent(5)
    site_info = {'site_mode': 'cms', 'sidebar': 'left'}
    to_view =  Context(dict(list(content.items()) + list(site_info.items() + 
                            list(sidebar.items()))))
    return render(request, 'cms/content.html', to_view)