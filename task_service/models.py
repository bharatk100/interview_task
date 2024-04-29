from django.db import models
from core.models import User
from project_service.models import Project

PRIORITY = [
    ("low", "Low"),
    ("medium", "Medium"),
    ("high", "High")
]

STATUS = [
    ("todo","Todo"),
    ("inprogress","InProgress"),
    ("done","done"),
    ("closed","closed"),
]

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField(max_length=191, choices=PRIORITY, null=True, default="low", blank=True)
    status = models.CharField(max_length=191, choices=STATUS, null=True, default="todo", blank=True)
    due_date = models.DateField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField(auto_now=True)

    class Meta:
        db_table = "tasks"