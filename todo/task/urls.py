from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_index, name='task_index'),
    path('delete/<int:task_id>/', views.task_delete, name='task_delete'),
    path('edit/<int:task_id>/', views.task_edit, name='task_edit'),
    path('update/<int:task_id>/', views.task_update, name='task_update'),
]