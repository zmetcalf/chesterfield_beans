from django.shortcuts import get_object_or_404

from cms.models import Content

def get_content(content_id):
    # TODO Possible reduction of code by passing content object in return
    content_object = get_object_or_404(Content, pk = content_id)
    content = content_object.content
    post_date_time = content_object.content_post_date
    title = content_object.title
    author = content_object.author.get_full_name()
    meta_keywords = content_object.seo_keywords
    meta_description = content_object.seo_description
    
    return {'content': content, 'author': author, 'post_date_time': 
            post_date_time, 'title': title, 'meta_keywords': meta_keywords,
            'meta_description': meta_description}
            
def get_recent():
    latest_content_list = Content.objects.all().order_by("-content_post_date")[:5]
    return {'latest_content_list': latest_content_list}