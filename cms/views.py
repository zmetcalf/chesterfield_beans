from django.shortcuts import render, get_object_or_404
from django.template import Context

from blog import blog_entry
from cms import cms_content
from cms.models import Content


def show_cms(request, content_id):
    content = content = get_object_or_404(Content, pk = content_id)
    sidebar = blog_entry.get_recent(5)
    site_info = {'site_mode': 'cms', 'sidebar': 'left', 'content': content}
    to_view =  Context(dict(list(site_info.items() + list(sidebar.items()))))
    return render(request, 'cms/content.html', to_view)