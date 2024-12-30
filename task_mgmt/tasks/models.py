from django.db import models

# Create your models here.
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
    due_date= models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    priority_level = models.CharField(max_length=10, choices=PRIORITY_LEVELS, default='low')
    status = models.CharField(max_length=15, choices=STATUS, default='pending')

    def __str__(self):
        return self.title