from asyncio.windows_events import NULL
import email
from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .models import *




# Create your views here.
def index(request):
    return render(request,'app/index.html')

def login(request):
    return render(request,'app/login.html')

def signup(request):
    return render(request,'app/signup.html')

# Notic: Firstly make sure that you are connected with mysql database. If not so connect the databse by setting.py in project. 
# Step 1 - Go to setting.py 
# Step 2 - Search the 'DATABASES' dic.
# Step 3 - Past the step-4  in 'DATABASES'
#------------- Step 4 ------------------------ 
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'music_player',   #database name
#         'USER': 'root',     #database user name
#         'PASSWORD' : 'password',  #database password
#         'HOST': 'localhost',    #database host name
#         'PORT': '3306' #database post 3306
#     }
# } 


def signup_data(request):
    name = request.POST.get("Name",False)
    email = request.POST.get("email",False)
    password = request.POST.get("password",False)
    password2 = request.POST.get("confirm_password",False)

    user = Candidate.objects.filter(email=email)

    if user:
        msg = "User already register"
        return render(request,'app/signup.html',{"msg":msg})
    else:
        if password == password2:
            newuser = Candidate.objects.create(name=name,email=email,password=password)
            msg = "Successfully Register"
            return render(request,'app/signup.html',{"msg":msg})
        else:
            msg = "Password is not same "
            return render(request,'app/signup.html',{"msg":msg})
    

def login_data(request):
    try:
        username = request.POST.get("username",False)
        password = request.POST.get("password",False)

        user = Candidate.objects.get(email=username)
        if user:
            if user.password == password:
                msg = user.name
                return render(request,'app/index.html',{"msg":msg})
            else:
                msg = "Password Incorrect "
                return render(request,'app/login.html',{"msg":msg})
        else:
            msg = "User Not Found"
            return render(request,'app/login.html',{"msg":msg})
    except:
        mssg = "User Not Found"
        return render(request,'app/login.html',{'msg':mssg})

