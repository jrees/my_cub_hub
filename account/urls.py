from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # login / logout urls
    # url(r'^login/$', auth_views.login, name='login'),
    # above is the old way, but this does not redirect if already logged in.
    # below is the new django 1.11 way which does redirect
    url(r'^login/',
        auth_views.LoginView.as_view(redirect_authenticated_user=True),
        name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^logout-then-login/$', auth_views.login, name='logout_then_login'),
    url(r'^$', views.dashboard, name='dashboard'),

    # change password urls
    url(r'^password-change/$', auth_views.password_change,
        name='password_change'),
    url(r'^password-change/done/$',
        auth_views.password_change_done,
        name="password_change_done"),

    # restore password urls
    url(r'^password-reset/$',
        auth_views.password_reset,
        name="password_reset"),
    url(r'^password-reset/done/$',
        auth_views.password_reset_done,
        name="password_reset_done"),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        auth_views.password_reset_confirm,
        name='password_reset_confirm'),
    url(r'^password-reset/complete/$',
        auth_views.password_reset_complete,
        name="password_reset_complete"),

    # user registration urls
    url(r'^register/$', views.register, name='register'),
    url(r'^parent_register', views.parent_register, name='parent_register'),
    url(r'^childminder_register', views.childminder_register, name='childminder_register'),

    # edit user profile
    url(r'^edit/$', views.edit, name='edit'),

    url(r'^dashboard/$', views.dashboard, name='dashboard')

    ]