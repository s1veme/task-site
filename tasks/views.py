from typing import List
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

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


class TasksNoCompletedView(ListAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.exclude(pk__in=self.request.user.tasks.values_list('pk', flat=True))


class TasksCompletedView(ListAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return self.request.user.tasks.all()
