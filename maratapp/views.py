# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person

# Create your views here.
def index(request):
    return render(request, 'marat.html', {'ob': Person.objects.all()})
def detail(request, person_id):
    return render(request, 'base.html', {'a': Person.objects.get(pk=person_id)})
def add_shit(request):
    return render(request, 'adduser.html')

def add_action(request):
    if request.method == 'GET':
        return HttpResponse("Dont fuck my server, fucking hacker!")
    elif request.method == 'POST':
        Person(first_name=request.POST['fname'], last_name=request.POST['lname']).save()
        return redirect('/')