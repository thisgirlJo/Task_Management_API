# Generated by Django 5.1.4 on 2025-01-08 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_tasks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='tasks',
        ),
    ]
