from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class AuthTests(TestCase):

    def test_user_can_register(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'testpass123',
            'password2': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(CustomUser.objects.filter(username='newuser').exists())

    def test_user_can_login(self):
        CustomUser.objects.create_user(username='testuser', password='testpass123')
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)  # redirect after login

    def test_login_fails_with_wrong_credentials(self):
        CustomUser.objects.create_user(username='anotheruser', password='correctpass')
        response = self.client.post(reverse('login'), {
            'username': 'anotheruser',
            'password': 'wrongpass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please enter a correct username and password", status_code=200)

class LogoutTest(TestCase):

    def test_user_can_logout(self):
        # تسجيل دخول المستخدم أولاً
        CustomUser.objects.create_user(username='logoutuser', password='logoutpass123')
        self.client.login(username='logoutuser', password='logoutpass123')

        # تنفيذ تسجيل الخروج
        response = self.client.get(reverse('logout'))

        # التأكد من إعادة التوجيه لصفحة تسجيل الدخول
        self.assertRedirects(response, reverse('login'))

        # التأكد من أن المستخدم لم يعد مسجلاً في الجلسة
        response2 = self.client.get(reverse('dashboard'))
        self.assertRedirects(response2, f"{reverse('login')}?next={reverse('dashboard')}")
