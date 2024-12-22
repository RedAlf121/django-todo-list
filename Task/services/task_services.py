from Task.models import Task
from django.contrib.auth.models import User

def getTask(user: User, id: int):
    pass

def listTask(user: User):
    return Task.objects.filter(user=user)

def addTask(form):
    user = User.objects.get(id=2)
    task = form.save(commit=False)
    task.user = user
    task.save()
    return task

def updateTask(user: User, task: Task, id: int):
    pass

def deleteTask(id: int):
    deleted=Task.objects.filter(id=id)
    return deleted.delete()