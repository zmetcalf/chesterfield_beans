from django.db import models

class SiteVariable(models.Model):
    
    def __unicode__(self):
        return self.option_variable
    
    option_name = models.CharField(max_length=20)       
    option_variable = models.CharField(max_length=50)
    
