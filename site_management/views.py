from django.shortcuts import render, get_object_or_404
from django.template import Context

from cms import cms_content
from site_management.models import SiteVariable

def base(request):
    title = get_object_or_404(SiteVariable, option_name__exact='Site Name')
    return render(request, 'base.html', {'title': title})

def show_cms(request, content_id):
    site_title = "Chesterfield Beans"
    content = cms_content.get_content(content_id)
    header = {'site_title': site_title}
    to_view =  Context(dict(list(content.items()) + list(header.items())))
    return render(request, 'cms.html', to_view)