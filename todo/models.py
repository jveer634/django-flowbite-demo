from django.db import models
from django.urls import reverse



class Todo(models.Model):

    STATUS_CHOICES = {
        "To Do":"To Do",
        "In Progress": "In Progress",
        "Completed":"Completed",
    }

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    content = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=11, default=STATUS_CHOICES["To Do"])


    def get_absolute_url(self):
        return reverse("todo:detail", kwargs={"id": self.id})
    
    def __str__(self) -> str:
        return self.title