from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='login'),
    path('home/',home,name='home'),
    path('task/add/', add_task,name='add_task'),
    path('task/delete/<int:id>/', delete_task,name='delete_task')
]