from django.urls import path
from . import views

urlpatterns = [
    path('tableau/', views.tableau_securite, name='tableau_securite'),
    path('conformite/', views.conformite, name='conformite'),
]