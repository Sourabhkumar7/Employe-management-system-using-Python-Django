from django.shortcuts import render,redirect
from django.http import HttpResponse
from employapp.models import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .helper import send_forgot_password
from .helper import *
import uuid
    

def register(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        number=request.POST.get("number")
        age=request.POST.get("age")
        dob=request.POST.get("DOB")
        password=request.POST.get("Password")
        confirm_password=request.POST.get("confirm_Password")
        if password != confirm_password:
            message.error(request,"password not matched")
        else:
            user=User.objects.create_user(username=number,password=password,email=email)
            user.first_name=name
            user.save()
            message.success(request,"registered successfully")
            return redirect("/login/")
    
    return render(request,"register.html")

def login1(request):
    
    if request.method=="POST":
        a=request.POST.get("number")
        b=request.POST.get("Password")
        user=authenticate(request,username=a,password=b)
        if user is not None:
            login(request,user)
            messages.success(request,"login successfully")
            return redirect("/")
        else:
            messages.error(request,"password and username is incorrect")
            return redirect("/login/")
      
    return render(request,"login.html")

def logout1(request):
    logout(request)
    return redirect("/login/")


@login_required(login_url="/login/")
def home(request):
    return render(request,"home.html")



def add_details(request):
    
    if request.method=="POST":
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
    
        salary=request.POST.get("salary")
        bonus=request.POST.get("bonus")
      
        phone=request.POST.get("phone")
        hire_date=request.POST.get("hire_date")
        
        a=Employe.objects.create(firstname=firstname,lastname=lastname,salary=salary,bonus=bonus,phone=phone,hire_date=hire_date)
        a.save()
    return render(request,"add_details.html")



def remove_details(request,emp_id=0):
   
    if emp_id:
        try:
            removed=Employe.objects.filter(id=emp_id)
            removed.delete()
            return HttpResponse("removed succeesfully")
        except:
            return HttpResponse("select again")
    emps=Employe.objects.all()
    context={"emps":emps}
    return render(request,"remove_details.html",context)



def view_details(request):
    
    a=Employe.objects.all()
    context={"emps":a}
    return render(request,"view_details.html",context)



def filter_details(request):
    
    if request.method=="POST":
        a=request.POST.get("firstname")
        b=request.POST.get("phone")
        c=Employe.objects.all()
        if a:
            c=c.filter(firstname__icontains=a) 
        if b:
            c=c.filter(phone__icontains=b)
        context={"sourabh":c}
        return render(request,"view_details.html",context)
    return render(request,"filter_details.html")


def forgot_password(request):
    if request.method=="POST":
        a=request.POST.get("username")
        user=User.objects.filter(username=a).exists()
        token=str(uuid.uuid4())
        
        a=Passw.objects.create(user=user)
        a.token=token
        a.save()
       
        send_forgot_password(user.email,token)
        message.success(request,"an email is sent")
        return redirect("/forgot_password/")
        
    return render(request,"forgot_password.html")

def change_password(request,token):
    ab=Passw.objects.filter(token=token).exists()
    context={"user_id":ab.user.id}
    a=request.POST.get("password")
    b=request.POST.get("password1")
    user_id=request.POST.get("user_id")
    if user_id is not None:
        a=User.objects.get(id=user_id)
        a.save()
        return redirect("/login/")
            
    
    return render(request,"change_password",context)