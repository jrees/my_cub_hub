
from django.forms import inlineformset_factory, ModelForm
from .models import Assessment, Hazard
from django.shortcuts import render

class AssessmentForm(ModelForm):
    class Meta:
        model = Assessment
        exclude = ()

HazardFormSet = inlineformset_factory(Assessment, Hazard, fields=['hazard_name',
                                                                  'possible_risk',
                                                                  'possible_consequences',
                                                                  'preControls',
                                                                  'postControls',
                                                                  'date_to_be_completed'],
                                      extra=1, can_delete=True, can_order=True)