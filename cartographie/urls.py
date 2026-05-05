from django.urls import path
from . import views

urlpatterns = [
    path('carte/', views.carte_tribunaux, name='carte_tribunaux'),
]