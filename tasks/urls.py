from django.urls import path

from .views import TasksView, TaskDetailView, TasksCompletedView, TasksNoCompletedView

urlpatterns = [
    path('', TasksView.as_view(), name='tasks'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task-update'),
    path('completed/', TasksCompletedView.as_view()),
    path('no-completed/', TasksNoCompletedView.as_view())
]
