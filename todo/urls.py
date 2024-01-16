from django.urls import path
from .views import TodoList, TodoDetail, TodoDeleteView, TodoCreate, TodoUpdate

app_name="todo"

urlpatterns = [
    path("", TodoList.as_view(), name="list"),
    path("new/", TodoCreate.as_view(), name="create"),
    path("<int:id>/", TodoDetail.as_view(), name="detail"),
    path("<int:id>/delete", TodoDeleteView.as_view(), name="delete"),
    path("<int:id>/update", TodoUpdate.as_view(), name="update"),
]
