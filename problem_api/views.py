# problem_api/views.py

import asyncio
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_problem(request):
    # 비동기 작업 생성
    create_problem_async()
    return JsonResponse({"message": "Problem creation started."})

@csrf_exempt
def check_problem(request, problem_id):
    # 임의의 문제 상태 확인
    problem_status = "solved" if problem_id == 1 else "unsolved"
    return JsonResponse({"status": problem_status})

# 비동기 작업 실행
def create_problem_async():
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.send)('problem-creation', {'type': 'create_problem'})
