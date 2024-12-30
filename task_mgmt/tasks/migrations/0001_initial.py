# Generated by Django 5.1.4 on 2024-12-30 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('due_date', models.DateTimeField()),
                ('priority_level', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='low', max_length=10)),
                ('status', models.CharField(choices=[('pending', ' Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='pending', max_length=15)),
            ],
        ),
    ]
