from django.contrib.auth.models import User
from django.contrib.auth import authenticate
def create_user(body: dict):
    print(body)
    user = User.objects.create_user(username=body['username'],\
                             email=body['email'],\
                                password=body['password'])
    return user

def find_user(request,body:dict):
    print(body)
    user = authenticate(request,username=body['username'],password=body['password'])
    
    print(user)
    return user