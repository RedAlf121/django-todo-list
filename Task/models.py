from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200,default='task')
    description = models.TextField(blank=True)
    date = models.DateField(null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " by " + self.user.username + " on " + self.date.strftime("%a, %d/%m/%Y")