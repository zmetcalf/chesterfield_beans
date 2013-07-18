from django.shortcuts import get_object_or_404

from site_management.models import SiteVariable

def global_context(request):
    return {
        "site_title": get_object_or_404(SiteVariable, option_name__exact='Site Name'),
        "site_slogan": get_object_or_404(SiteVariable, option_name__exact='Site Slogan'),
        "ip_address": request.META['REMOTE_ADDR']
    }