from django.db.models import fields
from django.http import request
from rest_framework import serializers

from user.models import User
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name_task', 'task_text', 'number_of_points')


class TaskDetailSerializer(serializers.ModelSerializer):
    completed = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        self.user = kwargs['context']['request'].user
        super().__init__(*args, **kwargs)

    class Meta:
        model = Task
        fields = ('id', 'name_task', 'task_text',
                  'number_of_points', 'completed')

    def get_completed(self, obj):
        return self.user.__class__.objects.filter(tasks=obj).exists()
