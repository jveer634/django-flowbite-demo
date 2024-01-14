from django.urls import path
from .views import TodoList, TodoDetail, TodoDeleteView

app_name="todo"

urlpatterns = [
    path("", TodoList.as_view(), name="list"),
    path("<int:id>/", TodoDetail.as_view(), name="detail"),
    path("<int:id>/delete", TodoDeleteView.as_view(), name="delete"),
]
