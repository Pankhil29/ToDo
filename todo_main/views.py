from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-update_at') # for - is descending order
    context = {
        'tasks' : tasks,
    }
    return render(request, "home.html",context)