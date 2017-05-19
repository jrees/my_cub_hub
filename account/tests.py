from django.test import TestCase
from django.core.urlresolvers import resolve
from .views import dashboard


# Create your tests here.
class UrlTests(TestCase):

    def test_root_url(self):
        found = resolve('/')
        # line below uses the url_name, whereas the line after uses func, both seem to work
        # self.assertEqual(found.url_name, 'dashboard')
        self.assertEquals(found.func, dashboard)

        # xxx   