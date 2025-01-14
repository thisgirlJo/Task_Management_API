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
    
    # Ensures proper updates
    def update(self, instance, validated_data):
        title = validated_data.pop('title')
        description = validated_data.pop('description')
        due_date = validated_data.pop('due_date')
        priority_level = validated_data.pop('priority_level')
        status = validated_data.pop('status')
        instance.title = title
        instance.description = description
        instance.due_date = due_date
        instance.priority_level = priority_level
        instance.status = status
        instance.save()
        return instance

    # Automatically sets the current user as the task owner when creating a task.
    def create(self, validated_data):
        return Task.objects.create(**validated_data)

class UserSerializer(serializers.ModelSerializer):          # Nested Serializer
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'tasks']