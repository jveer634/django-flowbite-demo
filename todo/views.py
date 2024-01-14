from django.views.generic import ListView, DetailView, DeleteView


from .models import Todo

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

