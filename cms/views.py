from django.shortcuts import render, get_object_or_404

def show_content(request, content_id):
    content_object = get_object_or_404(Content, pk = content_id)
    content = content_object.content
    return render(request, 'cms/content.html', {'content', content})

