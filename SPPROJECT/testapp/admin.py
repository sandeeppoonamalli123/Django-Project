from django.contrib import admin
from testapp.models import *

# Register your models here.
class HydJobsAdmin(admin.ModelAdmin):
    list_display=["date","company","eligibility","title","email","phone","address"]



admin.site.register(HydJobs,HydJobsAdmin)    
