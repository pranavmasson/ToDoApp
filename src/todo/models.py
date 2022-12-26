from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    due_date = models.CharField(max_length=20)
    completed = models.BooleanField(default=False)
