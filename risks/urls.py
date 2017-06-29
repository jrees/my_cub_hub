from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^mine/$', views.ManageAssessmentListView.as_view(), name='manage_assessment_list'),
    url(r'^create/$', views.AssessmentCreateView.as_view(), name='assessment_create'),
    url(r'^(?P<pk>\d+)/edit/$', views.AssessmentUpdateView.as_view(), name='assessment_change'),
    url(r'^(?P<pk>\d+)/delete/$', views.AssessmentDeleteView.as_view(), name='assessment_delete'),
]