import json
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from .services.task_services import *
from .services.user_services import *
from .forms import TaskForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
# Create your views here.


def home_closure(function,*args,**kwargs):
    def apply(*args,**kwargs):
        try:
            function(*args,**kwargs)
            return redirect(home)
        except:
            return redirect(signup_page)
    return apply


    
def signup_page(request):
    return render(request,'login.html')

@login_required
def home(request):
    user = request.user
    task_list = listTask(user)
    return render(request,'home.html',{
        'todolist':task_list,
        'add_task_form': TaskForm
    })

@home_closure
@login_required
def add_task(request):
    task = addTask(request,TaskForm(request.POST))

@home_closure
@login_required
def delete_task(request,id):
    result = deleteTask(id)


def signin(request):
    body_dict = json.loads(request.body.decode('utf-8'))
    user = create_user(body_dict)
    user.save()
    login(request,user)
    response=JsonResponse({'success': True, 'redirect_url': reverse('home')}) # Redirect to home after signup
    print(f"response:{response}")
    return response
    

def signup(request):
    body_dict = json.loads(request.body.decode('utf-8'))
    user = find_user(request,body_dict)
    response=JsonResponse({'success': True, 'redirect_url': reverse('home')}) # Redirect to home after signup
    print(f"response:{response}")
    login(user=user,request=request)
    return response