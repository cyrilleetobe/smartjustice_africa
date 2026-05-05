from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cartographie/', include('cartographie.urls')),
    path('signalement/', include('signalement.urls')),
    path('securite/', include('securite.urls')),
    path('', include('dashboard.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('api/', include('api.urls')),
]