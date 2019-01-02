# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee

# Create your views here.

def index(request):
    emp = Employee.objects.all()
    context = {
        'name' : emp,
    }
    return render(request, 'page1/index.html', context)

def index2(request):
    #sal = int(sal)
    name=""
    sal=0
    if request.method == 'POST':
        name = str(request.POST['name1'])
        sal = int(request.POST['salary1'])
        emp = Employee(ename=name,salary=sal)
        emp.save()
        return redirect(index3)

def index3(request):
    emp = Employee.objects.all()
    context = {
        'name' : emp
    }
    return render(request, "page1/age_page.html",context)

def delete(request,name):
    get_name=(name)
    emp=Employee.objects.get(ename=str(name))
    emp.delete()
    #emp.save()
    return redirect(index3)

def update(request,name):
    emp=Employee.objects.get(ename=str(name))
    context = {
    'u_name' : name,
    'o_name' : name,
    'u_salary' : emp.salary
    }
    return render(request,'page1/update.html',context)

def success_update(request):
    if request.method == 'POST':
        o_name = request.POST['o_name']
        n_name = request.POST['n_name']
        n_salary = request.POST['n_salary']
        emp=Employee.objects.get(ename=str(o_name))
        emp.ename = n_name
        emp.salary = n_salary
        emp.save()
    return redirect(index3)
