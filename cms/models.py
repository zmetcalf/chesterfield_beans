from django.contrib.auth.models import User
from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=200)
    content_post_date = models.DateTimeField('date published', null=True,
                                                blank=True)
    content = models.TextField()
    summary = models.TextField()
    author = models.ForeignKey(User, null=True, blank=True)
    seo_keywords = models.CharField(max_length=160, null=True, blank=True)
    seo_description = models.CharField(max_length=160, null=True, blank=True)
    sidebar_right = models.BooleanField()
    url_slug = models.CharField(max_length=80)
    # TODO add tags, Haystack and Whoosh to handle search of content and tags
    
    def __unicode__(self):
        return self.title
        
def user_unicode_patch(self):
    return '%s %s' % (self.first_name, self.last_name)

User.__unicode__ = user_unicode_patch