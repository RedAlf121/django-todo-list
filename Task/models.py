from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200,default='task')
    description = models.TextField(blank=True)
    date = models.DateField(name="date task",null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)