from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User
from django.core.urlresolvers import resolve
from .views import dashboard


# Create your tests here.
class UrlTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='Mario', email='mario@mushroom.com', password='luigi'
        )

    def test_root_url(self):
        found = resolve('/')
        # line below uses the url_name, whereas the line after uses func, both seem to work
        # self.assertEqual(found.url_name, 'dashboard')
        self.assertEquals(found.func, dashboard)

    def test_dashboard_if_logged_in(self):
        c = Client()
        c.login(username='Mario', password='luigi')
        response = c.get('/')
        self.assertEquals(response.status_code, 200)

    def test_redirect_if_not_logged_in(self):
        c = Client()
        response = c.get('/')
        self.assertEquals(response.status_code, 302)


# test creating new user



# test logging in
# see for ideas http://stackoverflow.com/questions/22457557/how-to-test-login-process

# test logging out

# test editing profile
