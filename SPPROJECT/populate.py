import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","SPPROJECT.settings")

django.setup()


from testapp.models import *
from faker import Faker
from random import *
faker=Faker()
def phoneNumberGen():
    d1=randint(7,9)
    num=""+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)    

def populate(n):
    for i in range(n):
        fdate=faker.date()
        fcompany=faker.company()
        feligibility=faker.random_element(elements=("BTech","MTech","MCA"))
        ftitle=faker.random_element(elements=("Developer","Tester","DB"))
        femail=faker.email()
        fphone=phoneNumberGen()
        faddrs=faker.address()
        hydjob_records=HydJobs.objects.get_or_create(date=fdate,company=fcompany,eligibility=feligibility,title=ftitle,email=femail,phone=fphone,address=faddrs)


populate(20)

