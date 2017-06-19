from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Hazard
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Assessment


class ManageAssessmentListView(ListView):
    model = Assessment
    template_name = 'risks/manage/risks/list.html'

    def get_queryset(self):
        qs = super(ManageAssessmentListView, self).get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerEditMixin(object):
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(OwnerEditMixin, self).form_valid(form)


class OwnerAssessmentMixin(OwnerMixin):
    model = Assessment


class OwnerAssessmentEditMixin(OwnerAssessmentMixin, OwnerEditMixin):
    fields = ['assessment_name', 'location']
    success_url = reverse_lazy('manage_assessment_list')
    template_name = 'assessments/manage/assessment/form.html'


class ManageAssessmentListView(OwnerAssessmentMixin, ListView):
    template_name = 'risks/manage/risks/list.html'


class AssessmentCreateView(OwnerAssessmentEditMixin, CreateView):
    pass


class AssessmentUpdateView(OwnerAssessmentEditMixin, UpdateView):
    pass


class AssessmentDeleteView(OwnerAssessmentMixin, DeleteView):
    template_name = 'risks/manage/risks/delete,html'
    success_url = reverse_lazy('manage_assessment_list')