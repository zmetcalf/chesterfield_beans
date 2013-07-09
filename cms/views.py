from django.shortcuts import render, get_object_or_404

from cms.models import Content

def show_content(request, content_id):
    content_object = get_object_or_404(Content, pk = content_id)
    content = content_object.content
    post_date_time = content_object.content_post_date
    title = content_object.title
    author = content_object.author.get_full_name()
    
    return render(request, 'cms/content.html', {'content': content, 
                    'author': author, 'post_date_time': post_date_time,
                    'title': title})