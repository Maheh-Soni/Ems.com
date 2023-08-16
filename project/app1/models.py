from django.db import models

class AdminDataBase(models.Model):
    name=models.CharField(max_length=200,null=False,blank=False)
    email=models.EmailField(max_length=200,null=False,blank=False)
    contact=models.IntegerField(null=False,blank=False)
    Password=models.CharField(max_length=100,null=False,blank=False)


class UserDataBase(models.Model):
    uname=models.CharField(max_length=200,null=False,blank=False)
    uemail=models.EmailField(max_length=200,null=False,blank=False)
    ucontact=models.IntegerField(null=False,blank=False)
    uPassword=models.CharField(max_length=100,null=False,blank=False)


class QueryDataBase(models.Model):
    qname=models.CharField(max_length=200,null=False,blank=False)
    qaddress=models.CharField(max_length=200,null=False,blank=False)
    qemail=models.EmailField(max_length=200,null=False,blank=False)
    qphone=models.IntegerField()
    query=models.TextField(max_length=200,null=False,blank=False)