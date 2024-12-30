from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TaskViewSet
from django.contrib.auth.views import LoginView

router = DefaultRouter()

router.register('users', UserViewSet)
router.register('tasks', TaskViewSet)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login')
]

urlpatterns += router.urls