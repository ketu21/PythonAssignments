from django.shortcuts import render
from .models import UserRecords


def loginrequest(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = UserRecords.objects.get(username=username)
    if user.password == password:
        return render(request, 'Welcome.html', {'fname':user.fname,'lname':user.lname})
    else:
        return render(request, 'login.html', {'loginmessage': 'Invalid username/password'})


def register_user(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    if username in UserRecords.objects.all().values_list('username',flat=True):
        return render(request, 'register.html', {'signinmessage': "User name already taken."})
    else:
        obj = UserRecords(fname=fname, lname=lname, username=username, email=email, password=password)
        obj.save()
        return render(request, 'login.html', {})

def login(request):
    return render(request, 'login.html',{})


def register(request):
    return render(request, 'register.html',{})


