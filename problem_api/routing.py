# problem_api/routing.py

from django.urls import path
from . import consumers

websocket_urlpatterns = [
    # WebSocket 연결을 받아들일 경로
    path('ws/problem/', consumers.ProblemConsumer.as_asgi()),
]
