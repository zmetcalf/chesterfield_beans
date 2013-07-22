from django.contrib.auth.models import User
from django.db import models

class BlogInfo(models.Model):
    title = models.CharField(max_length=200)
    tagline = models.CharField(max_length=200)
    url_slug = models.CharField(max_length=80)
    
    def __unicode__(self):
        return self.title
        
class BlogEntry(models.Model):
    blog_info = models.ForeignKey(BlogInfo)
    entry_title = models.CharField(max_length=200)
    entry_post_date = models.DateTimeField('date published', null=True,
                                                blank=True)
    entry = models.TextField()
    author = models.ForeignKey(User, null=True, blank=True)
    seo_keywords = models.CharField(max_length=160, null=True, blank=True)
    seo_description = models.CharField(max_length=160, null=True, blank=True)
    
    def __unicode__(self):
        return self.entry_title
        
def user_unicode_patch(self):
    return '%s %s' % (self.first_name, self.last_name)

User.__unicode__ = user_unicode_patch