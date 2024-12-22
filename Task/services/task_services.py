from Task.models import Task
from django.contrib.auth.models import User

def getTask(user: User, id: int):
    pass

def listTask(user: User):
    return Task.objects.all()

def addTask():
    pass

def updateTask(user: User, task: Task, id: int):
    pass

def deleteTask(user: User, id: int):
    pass