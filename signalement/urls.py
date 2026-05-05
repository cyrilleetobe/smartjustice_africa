from django.urls import path
from . import views

urlpatterns = [
    path('', views.formulaire_signalement, name='formulaire_signalement'),
    path('confirmation/<str:code>/', views.confirmation_signalement, name='confirmation_signalement'),
    path('suivi/', views.suivi_signalement, name='suivi_signalement'),
]