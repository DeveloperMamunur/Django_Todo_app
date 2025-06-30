from django.shortcuts import render

# Create your views here.

def task_index(request):
    return render(request, 'task/index.html')
