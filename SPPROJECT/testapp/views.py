from django.shortcuts import render
from testapp.models import HydJobs

# Create your views here.
def index(request):
    return render(request,"testapp/index.html")
def HydJobs_View(request):
    hydjobs_list=HydJobs.objects.all()
    return render(request,"testapp/results.html",{"hydjobs_list":hydjobs_list})
