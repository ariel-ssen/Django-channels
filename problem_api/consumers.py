# problem_api/consumers.py

import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer

class ProblemConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        pass

    async def create_problem(self, event):
        # 비동기 작업 실행
        await asyncio.sleep(5)
