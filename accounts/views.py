from django.shortcuts import render
from django.contrib.auth.models import User,auth
# Create your views here.


def register(request)
if request.method == 'POST'

    first_name = request.POST['first_name']


    user= User.objects.create_user(username=username,password=password1, email=email)
else:
    return render(request,'register.html')