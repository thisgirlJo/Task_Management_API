from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from .serializers import UserRegistrationSerializer, TaskSerializer, UserSerializer
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework.response import Response
from tasks.models import Task
from django.utils.timezone import now

User = get_user_model()

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'priority_level', 'due_date']
    ordering_fields = ['due_date', 'priority_level']

    """ def get_queryset(self):
        return Task.objects.filter(creator=self.request.user) """

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)     # Pass the user to the serializer
    
    @action(detail=True, methods=['patch'])
    def mark_complete(self, request, pk=None):
        task = self.get_object()
        task.status = True
        task.save()
        return Response({"message": "Task marked as complete"})

    @action(detail=True, methods=['patch'])
    def mark_incomplete(self, request, pk=None):
        task = self.get_object()
        task.status = False
        task.save()
        return Response({"message": "Task marked as incomplete"})

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]