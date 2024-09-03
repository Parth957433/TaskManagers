from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.filters(assigned_to=request.user)
    return render(request,'tasks/task_list.html',{'tasks' : tasks})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})


# Create your views here.
