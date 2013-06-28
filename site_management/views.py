from django.shortcuts import render, get_object_or_404

from site_management.models import SiteVariable

def base(request):
    title = get_object_or_404(SiteVariable, option_name__exact='Site Name')
    return render(request, 'base.html', {'title': title})
