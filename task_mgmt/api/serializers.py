from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from tasks.models import Task
from datetime import date

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        # Create User with a hashed password
        user = User.objects.create_user(
            #username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        user.is_active = True   # Automatically activate the user
        user.save()
        return user

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'priority_level', 'status']
        read_only_fields = ['created_at', 'updated_at', 'creator']

    # Validates the due date to ensure it is in the future.
    def validate_due_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("The due date must be in the future.")
        return value
    
    # Validates the priority level to ensure it is one of the allowed values.
    def validate_priority(self, value):
        priority_level = ['Low', 'Medium', 'High']
        if value not in allowed_priorities:
            raise serializers.ValidationError(f"Priority must be one of {priority_level}.")
        return value
    
    # Ensures Validation for proper status updates
    def validate_status(self, value):
        current_status = self.instance.status if self.instance else None
        allowed_transitions = {
            'Pending': ['In Progress'],
            'In Progress': ['Completed'],
            'Completed': []
        }

        if current_status and value not in allowed_transitions.get(current_status, []):
            raise serializers.ValidationError(
                f"Invalid status transition from {current_status} to {value}."
            )
        return value

    # Automatically sets the current user as the task owner when creating a task.
    def create(self, validated_data):
        return Task.objects.create(**validated_data)

class UserSerializer(serializers.ModelSerializer):          # Nested Serializer
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'tasks']