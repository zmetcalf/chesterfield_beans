from django.contrib import admin
from site_management.models import SiteVariable

class SiteVariableAdmin(admin.ModelAdmin):
    list_display = ('option_name', 'option_variable')

admin.site.register(SiteVariable, SiteVariableAdmin)
