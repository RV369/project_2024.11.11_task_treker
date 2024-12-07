from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('verified/', views.verified_task, name='verified'),
    path(
        'task_completed_cancellation/',
        views.task_completed_cancellation,
        name='task_completed_cancellation',
    ),
    path(
        'task_performer_cancellation/',
        views.task_performer_cancellation,
        name='task_performer_cancellation',
    ),
    path(
        'task_verified_cancellation/',
        views.task_verified_cancellation,
        name='task_verified_cancellation',
    ),
    path('performer/', views.appointed_performer, name='performer'),
    path('delete_task/', views.delete_task, name='delete_task'),
    path('completed/', views.task_completed, name='completed'),
    path('create/', views.create_task, name='new_task'),
    path('', views.show_tasks, name='index'),
]
