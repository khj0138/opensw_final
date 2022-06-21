from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('interest/', views.interest),
    path('basic/', views.basic),
    path('mbti/', views.mbti),
]
