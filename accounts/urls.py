from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import register, CustomLoginView, CustomLogoutView, dashboard

urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='registration/login.html',
            next_page='home'  # ✅ إعادة التوجيه بعد تسجيل الدخول
        ),
        name='login'
    ),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
]