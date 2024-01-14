from django.db import models
from django.urls import reverse



class Todo(models.Model):

    STATUS_CHOICES = [
        ("TD", "Todo"),
        ("IN", "In Progress"),
        ("CD", "Completed")
    ]

    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=128)
    content = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)

    def get_absolute_url(self):
        return reverse("todo:detail", kwargs={"pk": self.pk})
    