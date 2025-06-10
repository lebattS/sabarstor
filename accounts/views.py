from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'registration/logout.html'



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

import logging
logger = logging.getLogger(_name_)

def contact(request):
    logger.info("📨 Contact page accessed.")

def register(request):
    logger.info("📝 User registration page accessed.")

def login_view(request):
    logger.info("🔑 Login page accessed.")

def logout_view(request):
    logger.info("🚪 User logged out.")


