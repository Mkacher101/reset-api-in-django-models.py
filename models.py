from random import choices
from django.db import models
from datetime import date

# Create your models here.
class student(models.Model):#heritage
    name=models.CharField(max_length=70,null=False,blank=False)
    familyName=models.CharField(max_length=70,null=False,blank=False)
    birthDate=models.DateFeld(default=date(2004,1,1),null=False,blank=False)
    email=models.EmailField(maxlength=100)
    photo=models.ImageField(upload_to='photos/students',null=False,blank=False)
    stateC=[(present, absent, delayed,excluded)]
    state=models.CharField(choices=stateC,null=False,blank=False)
    situationC=[(new,repeating,derogatory,other)]
    situation=models.CharField(choices=situationC,null=False,blank=False)
    

class absence(models.Model):
    Date=models.DateField(default=date(2004,1,1),null=False,blank=False)
    motif=models.CharField()
    justification=models.DateFeld()


class session(models.Model):
    startime=models.TimeField(null=False,blank=False)
    endtime=models.TimeField(null=False,blank=False)
    classroomnumber=models.IntigerField()   
    goal=models.CharField(null=False,blank=False)
    summary=models.CharField(null=False,blank=False)
    tools=models.CharField()


class module(models.Model):
    Name=models.CharField(null=False,blank=False,unique=True)
    Nhours=models.IntegerFieldr(null=False,blank=False,unique=True)
    type=models.CharField()
    studylevel=[('1st','first class'),('2nd','second class'),('3rd','third class')]
    level=models.CharField(choices=studylevel)


class professor(models.Model):
    name=models.CharField(max_length=70,null=False,blank=False)
    familyName=models.CharField(max_length=70,null=False,blank=False)
    birthDate=models.DateFeld(default=date(2004,1,1),null=False,blank=False)
    personalemail=models.EmailField(maxlength=100)
    workemail=models.EmailField(maxlength=100)
    totalhoursofwork=models.IntegerField()
    photo=models.ImageField(upload_to='photos/prof')

class group(models.Model):
    name=models.CharField(max_length=70,null=False,blank=False) 
    nbstudent=models.IntigerField(null=False,blank=False)  
    email=models.EmailField(maxlength=100)
    studylevel=[('1st','first class'),('2nd','second class'),('3rd','third class')]
    level=models.CharField(choices=studentlevel)





