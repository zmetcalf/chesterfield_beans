from django import template

from blog import blog_entry

register = template.Library()

@register.inclusion_tag('sidebar.html')
def get_recent(entries):
    return blog_entry.get_recent(entries)
