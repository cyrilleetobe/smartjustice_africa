from django.urls import path
from . import views

urlpatterns = [
    path('tribunaux/', views.api_tribunaux, name='api_tribunaux'),
    path('stats/', views.api_stats, name='api_stats'),
    path('signalements/', views.api_signalements, name='api_signalements'),
]