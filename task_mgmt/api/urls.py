from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserRegistrationView, TaskViewSet, UserListView
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()

router.register('tasks', TaskViewSet)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='users'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
]

urlpatterns += router.urls