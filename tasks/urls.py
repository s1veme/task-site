from django.urls import path

from .views import TasksView, TaskDetailView

urlpatterns = [
    path('tasks/', TasksView.as_view(), name='tasks'),
    path('tasks/<int:pk>/', TaskDetailView.as_view())
]
