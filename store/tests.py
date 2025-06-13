from django.test import TestCase
from django.urls import reverse
from accounts.forms import CustomUserCreationForm
from django.contrib.auth.models import User

class UserRegistrationTests(TestCase):
    def test_register_view_accessible(self):
        """✅ صفحة التسجيل تفتح بشكل صحيح"""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_user_registration_success(self):
        """✅ يمكن تسجيل مستخدم جديد بنجاح"""
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'SuperSecure123!',
            'password2': 'SuperSecure123!',
        })
        self.assertEqual(response.status_code, 302)  # Redirect to login or dashboard
        self.assertTrue(User.objects.filter(username='newuser').exists())
