# problem_api/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('create_problem/', views.create_problem),
    path('check_problem/<int:problem_id>/', views.check_problem),
]
