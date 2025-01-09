from django.db import models
from users.models import User

class Task(models.Model):
    PRIORITY_LEVELS = (
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
    )

    STATUS = (
    ('pending', ' Pending'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed'),
    )

    title = models.CharField(max_length=20)
    description = models.TextField()
    due_date= models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    priority_level = models.CharField(max_length=10, choices=PRIORITY_LEVELS, default='low')
    status = models.CharField(max_length=15, choices=STATUS, default='pending')
    creator = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title