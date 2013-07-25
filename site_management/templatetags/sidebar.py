from django import template

from blog import blog_entry
from blog.models import BlogEntry

register = template.Library()

@register.inclusion_tag('sidebar.html')
def get_recent(entries):
    return blog_entry.get_recent(entries)

@register.simple_tag
def print_blog_entry_link(BlogEntry):
    year = BlogEntry.entry_post_date.year
    month= BlogEntry.entry_post_date.month
    day= BlogEntry.entry_post_date.day
    slug= BlogEntry.entry_slug
    link = "{0}/{1}/{2}/{3}/".format(year, month, day, slug)
    return link