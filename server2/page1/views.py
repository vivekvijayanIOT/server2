# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from .models import Employee
import time

# Create your views here.

session_key=0

def home(request):     # Home page to login the user
    global session_key
    context = {
    'date' : time.ctime()
    }
    if session_key==0:
        return render(request,'page1/home.html',context)
    else:
        return render(request,'page1/block.html',context)

def index(request):
    global session_key
    emp = Employee.objects.all()
    context = {
        'name' : emp,
    }
    if session_key==1:
        return render(request,'page1/index.html',context)
    else:
        return render(request,'page1/block.html',context)

def index2(request):
    global session_key
    #sal = int(sal)
    name=""
    sal=0
    if request.method == 'POST':
        name = str(request.POST['name1'])
        sal = int(request.POST['salary1'])
        emp = Employee(ename=name,salary=sal)
        emp.save()
        context={}
        if session_key==1:
            return redirect(index3)
        else:
            return render(request,'page1/block.html',context)

def index3(request):
    global session_key
    emp = Employee.objects.all()
    context = {
        'name' : emp
    }
    if session_key==1:
        return render(request,'page1/age_page.html',context)
    else:
        return render(request,'page1/block.html',context)

def delete(request,name):
    global session_key
    get_name=(name)
    try:
        emp=Employee.objects.get(ename=str(name))
    except(KeyError,Employee.MultipleObjectsReturned):
        return HttpResponse("Sorry some records are error")
    emp.delete()
    #emp.save()
    context={}
    if session_key==1:
        return redirect(index3)
    else:
        return render(request,'page1/block.html',context)

def update(request,name):
    global session_key
    emp=Employee.objects.get(ename=str(name))
    context = {
    'u_name' : name,
    'o_name' : name,
    'u_salary' : emp.salary
    }
    if session_key==1:
        return render(request,'page1/update.html',context)
    else:
        return render(request,'page1/block.html',context)

def success_update(request):
    global session_key
    if request.method == 'POST':
        o_name = request.POST['o_name']
        n_name = request.POST['n_name']
        n_salary = request.POST['n_salary']
        emp=Employee.objects.get(ename=str(o_name))
        emp.ename = n_name
        emp.salary = n_salary
        emp.save()
        context={}
    if session_key==1:
        return redirect(index3)
    else:
        return render(request,'page1/block.html',context)

def login_sites(request): #redirects to the usual page
    global session_key
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username = username , password = password)
        if user:
            login(request,user)
            session_key=1
            context = {
            'user' : username
            }
            return redirect(index)
        else:
            return HttpResponse("Sorry")
    return HttpResponse("sorry too")
