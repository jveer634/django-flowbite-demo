from django.urls import path
from .views import TodoList

app_name="todo"

urlpatterns = [
    path("", TodoList.as_view(), name="list")
]
