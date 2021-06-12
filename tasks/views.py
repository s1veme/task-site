from rest_framework import serializers
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import TaskSerializer, TaskDetailSerializer
from .models import Task


class TasksView(ListAPIView):
    permission_classes = [AllowAny, ]

    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskDetailView(RetrieveAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = TaskDetailSerializer
    queryset = Task.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


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
