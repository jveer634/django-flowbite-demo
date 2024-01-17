from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from .models import Todo
from .forms import TodoForm

class TodoList(ListView):
    model = Todo
    template_name="todo_list.html"


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

