from django.shortcuts import get_object_or_404

from cms.models import Content

def get_content(content_id):
    # TODO Possible reduction of code by passing content object in return
    content = get_object_or_404(Content, pk = content_id)
    return {'content': content}
            
def get_recent():
    latest_content_list = Content.objects.all().order_by("-content_post_date")[:5]
    return {'latest_content_list': latest_content_list}