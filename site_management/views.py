from django.shortcuts import render, get_object_or_404
from django.template import Context

from cms import cms_content
from site_management.models import SiteVariable

def show_cms(request, content_id):
    site_title = get_object_or_404(SiteVariable, option_name__exact='Site Name')
    site_slogan = get_object_or_404(SiteVariable, option_name__exact='Site Slogan')
    content = cms_content.get_content(content_id)
    header = {'site_title': site_title, 'site_slogan': site_slogan,
                'site_mode': "cms"}
    to_view =  Context(dict(list(content.items()) + list(header.items())))
    return render(request, 'cms/content.html', to_view)