from django.urls import path

from .views import LeaderTable

urlpatterns = [
    path('leaders/', LeaderTable.as_view())
]
