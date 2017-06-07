from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class RiskAssessment(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    created = models.DateField(auto_now_add=True)
    assessment_date = models.DateField(auto_now=True)

    class Meta:
        ordering = ('title',)


class Hazard(models.Model):
    risk_assessment = models.ForeignKey(RiskAssessment, related_name='hazards')
    hazard_name = models.CharField(max_length=200)
    possible_consequences = models.CharField(max_length=500)
    preControl = models.CharField(max_length=200)
    postControls = models.CharField(max_length=200)
    date_to_be_completed = models.DateField()