from django.urls import path

from .views import LeaderTableView

urlpatterns = [
    path('leaders/', LeaderTableView.as_view())
]
