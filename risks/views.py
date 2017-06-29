from django.shortcuts import render
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Assessment
from braces.views import LoginRequiredMixin, PermissionRequiredMixin


class ManageAssessmentListView(ListView):
    model = Assessment
    template_name = 'risks/list.html'

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


class OwnerAssessmentMixin(OwnerMixin, LoginRequiredMixin):
    model = Assessment
    fields = ['assessment_name', 'location']
    success_url = reverse_lazy('manage_assessment_list')


class OwnerAssessmentEditMixin(OwnerAssessmentMixin, OwnerEditMixin):
    fields = ['assessment_name', 'location']
    success_url = reverse_lazy('manage_assessment_list')
    template_name = 'risks/form.html'


class ManageAssessmentListView(OwnerAssessmentMixin, ListView):
    template_name = 'risks/list.html'


class AssessmentCreateView(PermissionRequiredMixin, OwnerAssessmentEditMixin, CreateView):
    permission_required = 'risks.add_assessment'


class AssessmentUpdateView(PermissionRequiredMixin, OwnerAssessmentEditMixin, UpdateView):
    template_name = 'risks/form.html'
    permission_required = 'risks.change_assessment'


class AssessmentDeleteView(PermissionRequiredMixin, OwnerAssessmentMixin, DeleteView):
    template_name = 'risks/delete.html'
    success_url = reverse_lazy('manage_assessment_list')
    permission_required = 'risks.delete_risk'


