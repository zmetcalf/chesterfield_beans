from django.shortcuts import get_object_or_404

from cms.models import Content
            
def get_recent():
    latest_content_list = Content.objects.all().order_by("-content_post_date")[:5]
    return {'latest_content_list': latest_content_list}