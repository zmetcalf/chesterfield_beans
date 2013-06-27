from django.db import models

class SiteVariables(models.Model):
    
    def __unicode__(self):
        return self.site_name
        
    site_name = models.CharField(max_length=50)
