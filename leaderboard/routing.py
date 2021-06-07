import leaderboard
from django.urls import re_path

from .consumers import LeadersConsumers

websocket_urlpatterns = [
    re_path('ws/leaderboard/', LeadersConsumers.as_asgi())
]
