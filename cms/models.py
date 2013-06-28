from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=200)
    content_post_date = models.DateTimeField('date published')
    # TODO add tags, Haystack and Whoosh to handle search of content and tags
    
class Comment(models.Model):
    content = models.ForeignKey(Content)
    subject = models.CharField(max_length=200)
    comment = models.CharField(max_length=1000)
    comment_post_date = models.DateTimeField('date published')
