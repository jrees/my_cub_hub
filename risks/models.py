from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


def get_month_from_now():
    return datetime.today() + timedelta(days=30)


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Assessment(BaseModel):
    owner = models.ForeignKey(User, related_name='assessments_created')
    assessment_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.assessment_name


class Hazard(BaseModel):
    assessment = models.ForeignKey(Assessment, related_name='hazards')
    hazard_name = models.CharField(max_length=50)
    possible_risk = models.TextField(default='')
    possible_consequences = models.TextField(default='')
    preControls = models.CharField(max_length=200, default='')
    postControls = models.CharField(max_length=200, default='')
    date_to_be_completed = models.DateField(default=get_month_from_now())

    def __str__(self):
        return self.hazard_name