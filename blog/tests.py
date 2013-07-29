from django.contrib.auth.models import User
from django.test import TestCase

from blog.models import BlogEntry, BlogInfo

class BlogInfoTestCase(TestCase):
    
    def setUp(self):
        BlogInfo.objects.create(title="Test Blog", tagline="This is just a test", url_slug="test-slug")
        
    def test_values_taken(self):
        test_blog = BlogInfo.objects.get(pk=1)
        self.assertEqual(test_blog.title, "Test Blog")
        self.assertEqual(test_blog.tagline, "This is just a test")
        self.assertEqual(test_blog.url_slug, "test-slug")
        
class BlogEntryTestCase(TestCase):
    
    def setUp(self):
        blog_info_object = BlogInfo.objects.create(title="Test Blog", 
            tagline="This is just a test", url_slug="test-slug")
        user = User.objects.create_user('test', 'test@email.com', 'testword')
        BlogEntry.objects.create(blog_info=blog_info_object, entry_title="Blog Entry Title",
            entry_post_date='2011-09-01T13:20:30+03:00', entry="Here is the entry information",
            author=user, seo_keywords="SEO,keywords,for,site", 
            seo_description="Description for the site SEO Style", entry_slug="entry-test")
        
    def test_values_taken(self):
        test_entry = BlogEntry.objects.get(pk=1)
        self.assertEqual(test_entry.entry_title, "Blog Entry Title")
        