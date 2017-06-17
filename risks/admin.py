from django.contrib import admin
from .models import Assessment, Hazard


# Register your models here.
@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ['assessment_name', 'location', 'created_date', 'modified_date']


class HazardAdmin(admin.ModelAdmin):
    list_display = ['hazard_name']