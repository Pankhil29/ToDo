from django.http import HttpResponse
from django.shortcuts import render
from .models import Task
from django.shortcuts import redirect

# Create your views here.
def addTask(req):
    task = req.POST['task']
    Task.objects.create(task=task)
    return redirect("home")