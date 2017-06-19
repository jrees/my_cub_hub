from django.contrib import admin
from .models import Assessment, Hazard

# see https://docs.djangoproject.com/en/1.11/ref/contrib/admin/
# this sets up how the models are viewed in the admin site.
# Register your models here.
@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ['assessment_name', 'location', 'created_date', 'modified_date']

@admin.register(Hazard)
class HazardAdmin(admin.ModelAdmin):
    list_display = ['hazard_name']