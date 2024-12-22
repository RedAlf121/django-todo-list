from django.urls import path
from .views import *

urlpatterns = [
    path('', signup_page, name='start'),
    path('login/',signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('home/',home,name='home'),
    path('task/add/', add_task,name='add_task'),
    path('task/delete/<int:id>/', delete_task,name='delete_task')
]