from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, CompletedTask, AppointedPerformer, VerifiedTask
from .forms import TaskForm, AppointedPerformerForm, VerifiedTaskForm
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .core import employee_selection

User = get_user_model()


def show_tasks(request):
    form_performers = AppointedPerformerForm()
    form_reviewers = VerifiedTaskForm()
    page_number = request.GET.get('page')
    page_obj = Paginator(
        Task.objects.all(), 3).get_page(page_number)
    context = {
        'page_obj': page_obj,
        'form_reviewers': form_reviewers,
        'form_performers': form_performers,
    }
    return render(request, 'tasks/index.html', context) 

@login_required
def appointed_performer(request):
    form_performers = AppointedPerformerForm(request.POST or None)
    if request.method == 'POST':
        if form_performers.is_valid():
            if request.POST.get("performer") == '':
                pk = employee_selection()
            else:
                pk = request.POST.get("performer")
            task = get_object_or_404(
                Task, pk=request.POST.get("task_id"))
            performer = get_object_or_404(
                User, pk=pk)
            AppointedPerformer.objects.get_or_create(
                task=task, performer=performer)
    return redirect('tasks:index')

@login_required
def task_completed(request):
    if request.method == 'POST':
        task = get_object_or_404(
            Task, pk=request.POST.get('task_id'))
        task_completed = get_object_or_404(
            AppointedPerformer, task=task)
        CompletedTask.objects.get_or_create(
            task_completed=task, 
            performer_task_completed=task_completed)
    return redirect('tasks:index')

@login_required
def task_completed_cancellation(request):
    if request.POST.get('delete'):
        task = get_object_or_404(
            Task, pk=request.POST.get('delete'))
        object_delete = get_object_or_404(
            CompletedTask, task_completed=task)
        object_delete.delete()
    return redirect('tasks:index')

@login_required
def task_performer_cancellation(request):
    if request.POST.get('delete'):
        task = get_object_or_404(
            Task, pk=request.POST.get('delete'))
        object_delete = get_object_or_404(
            AppointedPerformer, task=task)
        object_delete.delete()
    return redirect('tasks:index')

@login_required
def task_verified_cancellation(request):
    if request.POST.get('delete'):
        task = get_object_or_404(
            Task, pk=request.POST.get('delete'))
        object_delete = get_object_or_404(
            VerifiedTask, task_verified=task)
        object_delete.delete()
    return redirect('tasks:index')

@login_required
def verified_task(request):
    form_reviewers = VerifiedTaskForm(request.POST or None)
    if request.method == 'POST':
        if form_reviewers.is_valid():
            if request.POST.get("reviewer") == '':
                pk = request.user.pk
            else:
                pk = request.POST.get("reviewer")
        task = get_object_or_404(
            Task, pk=request.POST.get('task_id'))
        reviewer = get_object_or_404(User, pk=pk)
        task_completed = get_object_or_404(
            CompletedTask, task_completed=task)
        VerifiedTask.objects.get_or_create(
            task_verified=task, reviewer=reviewer, 
            verified_task_completed=task_completed)
    return redirect('tasks:index')

@login_required
def create_task(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.author_task = request.user
        task.save()
        return redirect('tasks:index')
    context = {'form': form}
    return render(request,'tasks/create_new_task.html', context)

@login_required
def delete_task(request):
    if request.POST.get('delete_task_id'):
        task_delete = get_object_or_404(
            Task, pk=request.POST.get('delete_task_id'))
        task_delete.delete()
    return redirect('tasks:index')
