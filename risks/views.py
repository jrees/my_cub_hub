from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Assessment
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic.base import TemplateResponseMixin, View
from .forms import AssessmentForm, HazardFormSet
from django.shortcuts import get_object_or_404, redirect


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


class AssessmentCreateView(PermissionRequiredMixin, OwnerAssessmentEditMixin, CreateView):
    permission_required = 'risks.add_assessment'


class AssessmentUpdateView(PermissionRequiredMixin, OwnerAssessmentEditMixin, UpdateView):
    template_name = 'risks/form.html'
    permission_required = 'risks.change_assessment'


class AssessmentDeleteView(PermissionRequiredMixin, OwnerAssessmentMixin, DeleteView):
    template_name = 'risks/delete.html'
    success_url = reverse_lazy('manage_assessment_list')
    permission_required = 'risks.delete_risk'


class AssessmentHazardUpdateView(TemplateResponseMixin, View):
    template_name = 'hazards/formset.html'
    assessment = None

    def get_formset(self, data=None):
        return HazardFormSet(instance=self.assessment, data=data)

    def dispatch(self, request, pk):
        self.assessment = get_object_or_404(Assessment, id=pk, owner=request.user)
        return super(AssessmentHazardUpdateView, self).dispatch(request, pk)

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'assessment': self.assessment, 'formset': formset})

    def post(self, request, *args, **kwargs):
        # TRY THIS
        form = AssessmentForm()
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('manage_assessment_list')
        return self.render_to_response({'assessment': self.assessment, 'formset': formset, 'form': form})
