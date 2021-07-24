from django.db import models
from django.db.models import DateTimeField
# Create your models here.

from django.contrib.auth.models import User

class projects(models.Model):
    project_name = models.CharField(max_length=200,verbose_name='Project Name',null=True,blank=True)
    users = models.ManyToManyField(User, blank=True, verbose_name='Users')
    created_by= models.ForeignKey(User, models.CASCADE, related_name='CreatedByuser',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False,blank=True,null=True)
    modified_at = models.DateTimeField(auto_now_add=False, auto_now=True,blank=True,null=True)

class Clients(models.Model):
    client_name = models.CharField(max_length=200,verbose_name='Client Name',null=True,blank=True)
    project = models.ManyToManyField(projects, blank=True, verbose_name='Project')
    created_by=models.ForeignKey(User, models.CASCADE,verbose_name='Created By',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False,blank=True,null=True)
    modified_at = models.DateTimeField(auto_now_add=False, auto_now=True,blank=True,null=True)
