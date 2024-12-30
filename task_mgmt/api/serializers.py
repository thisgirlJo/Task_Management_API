from rest_framework import serializers
from django.contrib.auth import get_user_model
from tasks.models import Task
from datetime import date

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'priority', 'status', 'created_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'owner']

    def validate(self, data):
        if data < date.today():
            raise serializers.ValidationError("Due date must be nin the future.")
        return data