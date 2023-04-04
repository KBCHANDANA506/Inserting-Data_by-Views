from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from app.models import *

def Insert_Topic(request):
    tn=input("enter Topic_name")
    TO=Topic.objects.get_or_create(Topic_name=tn)[0]
    TO.save()
    return HttpResponse("Data inserted successfully")

def insert_Webpage(request):
    tn=input("enter tn")
    N=input("enter name")
    U=input("enter Url")
    TO=Topic.objects.get_or_create(Topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(Topic_name=TO,Name=N,Url=U)[0]
    WO.save()
    return HttpResponse("Webpage data inserted successfully")



def Insert_AccessRecord(request):
    tn=input("enter tn")
    N=input("enter name")
    U=input("enter Url")
    A=input("enter author name")
    D=input("enter date")
    TO=Topic.objects.get_or_create(Topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(Topic_name=TO,Name=N,Url=U)[0]
    WO.save()
    AO=AccessRecord.objects.get_or_create(Name=WO,Author=A,Date=D)[0]
    AO.save()
    return HttpResponse("AccessRecord data inserted successfully")


    


