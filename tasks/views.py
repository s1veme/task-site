from typing import List
from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from .serializers import TaskSerializer
from .models import Task


class TasksView(ListAPIView):
    permission_classes = [AllowAny, ]

    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskDetailView(RetrieveAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
