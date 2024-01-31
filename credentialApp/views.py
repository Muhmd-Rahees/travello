from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth


# Create your views here.

def login(request):
    if request.method == 'POST':
        username00 = request.POST['username']
        password00 = request.POST['password']

        user = auth.authenticate(username = username00, password = password00)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"INVALID CREDENTIALS")
            return redirect('login')

    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        Ausername = request.POST['username']
        Afirst_name = request.POST['first_name']
        Alast_name = request.POST['last_name']
        Aemail = request.POST['email']
        Apassword = request.POST['password']
        Apassword1 = request.POST['password1']

        if Apassword == Apassword1 :

            if User.objects.filter(username = Ausername).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            
            elif User.objects.filter(email = Aemail).exists():
                messages.info(request,"Email Taken")
                return redirect("register")
            
            else:
                user = User.objects.create_user(username = Ausername,password = Apassword,first_name = Afirst_name,last_name = Alast_name,email = Aemail)
                user.save()
                print("*****user created*****")

        else:
            messages.info(request,"Password Not Matching")
            return redirect("register")
        return redirect('login')

    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
