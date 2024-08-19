from django.db import models

# Create your models here.
class HydJobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.CharField(max_length=100)
    