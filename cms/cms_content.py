from django.shortcuts import get_object_or_404

from cms.models import Content

def get_content(content_id):
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