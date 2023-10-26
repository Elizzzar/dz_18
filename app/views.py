from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView, ListView,DetailView
from .models import Task
from django.urls import reverse_lazy
from .forms import FormTask
# Create your views here.

# Домашнее задание №18 Контроллеры функций
# 1. Перепишите все оставшиеся контроллеры функции на классы.
# 2. Подготовьте классы для недостающих моментов.

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'task_list'
    context_object_name = 'tasks'
    #

class TaskCreateView(CreateView):
    model = Task
    form_class = FormTask
    template_name = 'task_create.html'
    success_url = reverse_lazy('task_list')
    #

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task_detail'
    #

class TaskUpdateView(UpdateView):
    model = Task
    form_class = FormTask
    template_name = 'task_update.html'
    success_url = reverse_lazy('task_list')
    #

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task_delete'
    success_url = reverse_lazy('task_list')
    #