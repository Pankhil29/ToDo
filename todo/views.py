from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Task
from django.shortcuts import redirect

# Create your views here.
def addTask(req):
    task = req.POST['task']
    Task.objects.create(task=task)
    return redirect("home")

def mark_as_done(req,pk):
    task = get_object_or_404(Task,pk=pk)
    # for finding a particular object based on primary key
    task.is_completed = True
    task.save()
    return redirect("home")

def mark_as_undone(req,pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = False
    task.save()
    return redirect("home")

def edit_task(req,pk):
    get_task = get_object_or_404(Task,pk=pk)
    if req.method == "POST":   
        new_task = req.POST['task']    # it give dictionary of data
        get_task.task = new_task
        get_task.save()
        return redirect("home")
    else:
        context = {
            'get_task':get_task
        }
    return render(req,'edit_task.html',context)

def delete_task(req,pk):
    task = get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('home')
    
    
# url -> views -> model -> database
# in html file we will call the url in buttons 

# get -> to fetch data from server or load the data
# post -> to send data to the server or updating data