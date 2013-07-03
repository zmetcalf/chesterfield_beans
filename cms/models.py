from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=200)
    content_post_date = models.DateTimeField('date published')
    content = models.TextField()
    # TODO add tags, Haystack and Whoosh to handle search of content and tags
