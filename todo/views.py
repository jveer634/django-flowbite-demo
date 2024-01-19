from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from .models import Todo
from .forms import TodoForm

class TodoList(ListView):
    model = Todo
    template_name="todo_list.html"

    def get_queryset(self) -> QuerySet[Todo]:
        qs = super().get_queryset()
        search = self.request.GET.get("search")
        status = self.request.GET.get("status")

        if search != "" and search is not None:
            qs = qs.filter(title__icontains=search)
        if status != "" and status is not None:
            qs = qs.filter(status = status)
        return qs


class TodoDetail(DetailView):
    model = Todo
    pk_url_kwarg="id"
    template_name="todo_detail.html"


class TodoDeleteView(DeleteView):
    model = Todo
    pk_url_kwarg="id"
    template_name = "todo_delete.html"
    
    def get_success_url(self):
        return reverse_lazy('todo:list')

class TodoCreate(CreateView):
    model = Todo
    template_name = "todo_create.html"
    pk_url_kwarg="id"
    form_class=TodoForm

class TodoUpdate(UpdateView):
    model = Todo
    form_class=TodoForm
    pk_url_kwarg="id"
    template_name = "todo_update.html"

