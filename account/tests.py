from django.test import TestCase
from django.core.urlresolvers import resolve
from django.conf.urls import url
from .views import dashboard

# Create your tests here.


class UrlTests(TestCase):

    def test_root_url(self):
        found = resolve('/')
        # line below uses the url_name, whereas the line after uses func, both seem to work
        # self.assertEqual(found.url_name, 'dashboard')
        self.assertEquals(found.func, dashboard)

# test that we are not loggedin that visiting /account/ takes us to login
# test that if we are logged in that visiting /account/ takes us to dashboard

# test edit profile

# test that we can create an account with valid info
# test what happens when we don't use valid information... is it what we want to happen

# test we can login with valid info
# test trying to login with wrong details

# test trying to reset a pw
# test trying to enter two different pw when setting a new password

