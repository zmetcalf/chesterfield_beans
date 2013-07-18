from django.shortcuts import get_object_or_404

from site_management.models import SiteVariable

def global_context(request):
    return {
        "SITE_TITLE": get_object_or_404(SiteVariable, option_name__exact='Site Name'),
        "SITE_SLOGAN": get_object_or_404(SiteVariable, option_name__exact='Site Slogan')
    }