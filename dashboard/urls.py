from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('dashboard/', views.dashboard_principal, name='dashboard'),
]