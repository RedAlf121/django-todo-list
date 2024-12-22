from django.shortcuts import render
from .models import Task
from .services.task_services import *
# Create your views here.
def home(request):
    user = User.objects.get(id=2)
    task_list = listTask(user)
    return render(request,'home.html',{'todolist':task_list})

def add_task(request):
    pass

def delete_task(request):
    pass

def update_task(request):
    pass

def login(request):
    pass