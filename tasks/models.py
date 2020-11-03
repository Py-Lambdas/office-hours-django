import uuid

from django.db import models


class Task(models.Model):
    class TaskPriority(models.TextChoices):
        URGENT = "U", "Urgent"
        HIGH = "H", "High"
        MEDIUM = "M", "Medium"
        LOW = "L", "Low"

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    description = models.TextField()
    complete = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=1, choices=TaskPriority.choices, default=TaskPriority.LOW
    )
    project = models.ForeignKey(
        "Project", on_delete=models.CASCADE, related_name="tasks", null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} <{self.priority}>"


class Project(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.TextField()

    def __str__(self):
        return f"{self.name} <Tasks: {self.tasks}>"
