from django.shortcuts import render, redirect
from .models import Task


# Create your views here.
def task_index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        task = Task.objects.create(title=title)
        task.save()
        return redirect('task_index')

    tasks = Task.objects.all()
    context = {'tasks': tasks}

    return render(request, 'task/index.html', context)


def task_delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_index')


def task_edit(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        task.title = title
        task.save()
        return redirect('task_index')


    context = {'task': task}
    return render(request, 'task/index.html', context)


def task_update(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_complete = not task.is_complete
    task.save()
    return redirect('task_index')