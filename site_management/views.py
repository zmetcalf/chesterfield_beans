from django.shortcuts import render, get_object_or_404

from site_management.models import SiteVariables

def base(request):
    title = get_object_or_404(SiteVariables, pk=site_name)
    return render(request, 'base.html', {'title': title})
