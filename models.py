from random import choices
from django.db import models
from datetime import date

# Create your models here.
class student(models.Model):#heritage
    name=models.CharField(max_length=70,null=False,blank=False)
    familyName=models.CharField(max_length=70,null=False,blank=False)
    birthDate=models.DateFeld(default=date(2004,1,1),null=False,blank=False)
    email=models.EmailField(maxlength=100)
    photo=models.ImageField(upload_to='photos/students')
class professor(models.Model):
    name=models.CharField(max_length=70,null=False,blank=False)
    familyName=models.CharField(max_length=70,null=False,blank=False)
    birthDate=models.DateFeld(default=date(2004,1,1),null=False,blank=False)
    email=models.EmailField(maxlength=100)
    photo=models.ImageField(upload_to='photos/students')

class group(models.Model):
    name=models.CharField(max_length=70,null=False,blank=False) 
    nbstudent=models.IntigerField(null=False,blank=False)  
    email=models.EmailField(maxlength=100)
    speciality=models.CharField(max_length=70,null=False,blank=False)
    studylevel=[('1st','first class','2nd','second class','3rd','third class')]
    level=models.CharField(choices=studentlevel)

class adress(models.Model):
    number=models.IntigerField(null=False,blank=False)   

class module(models.Model):
     modulename=[('Math','physique','francais','anglais','informatique','securite')]
     name=models.CharField(choices=modulename,max_length=70,null=False,blank=False)

class universite(models.Model):
    uniname=[('isg','ihec','fst','fseg','enit')]
    name=models.CharField(choices)uniname,max_length=70,null=False,blank=False) 





