from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
import logging

logger = logging.getLogger(_name_)

# ✅ لوحة التحكم (تتطلب تسجيل دخول)
@login_required
def dashboard(request):
    logger.info(f"👤 Dashboard accessed by user: {request.user}")
    return render(request, 'accounts/dashboard.html')

# ✅ تسجيل الدخول
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

# ✅ تسجيل الخروج
class CustomLogoutView(LogoutView):
    template_name = 'registration/logout.html'

# ✅ التسجيل
def register(request):
    logger.info("📝 User registration page accessed.")
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info("✅ New user registered successfully.")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})