from django.shortcuts import render, get_object_or_404

from cms.models import Content

def show_content(request):
    content_object = get_object_or_404(Content, pk = 1)
    content = content_object.content
    return render(request, 'cms/content.html', {'content': content})

