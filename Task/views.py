from django.shortcuts import render,redirect
from .services.task_services import *
from .forms import TaskForm
# Create your views here.

def home_closure(function,*args,**kwargs):
    def apply(*args,**kwargs):
        function(*args,**kwargs)
        return redirect(home)
    return apply
    

def home(request):
    user = User.objects.get(id=2)
    task_list = listTask(user)
    return render(request,'home.html',{
        'todolist':task_list,
        'add_task_form': TaskForm
    })

@home_closure
def add_task(request):
    task = addTask(TaskForm(request.POST))

@home_closure
def delete_task(request,id):
    result = deleteTask(id)

def login(request):
    pass