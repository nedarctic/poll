from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

# from .views import SignupPageView
# from .forms import CustomUserCreationForm

class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create(
            username = "testuser",
            email = "testuser@email.com",
            password = "testpass123"
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
    def test_create_superuser(self):
        User = get_user_model()
        admin = User.objects.create_superuser(
            username = "admin",
            email = "admin@email.com",
            password = "admipass123"
        )
        self.assertEqual(admin.username, "admin")
        self.assertEqual(admin.email, "admin@email.com")
        self.assertTrue(admin.is_active)
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)

"""
class SignupPageTests(TestCase):
    def setUp(self):
        url = reverse("signup")
        self.response = self.client.get(url)
    def test_signup_status_code(self):
        self.assertEqual(self.response.status_code, 200)
    def test_signup_uses_correct_template(self):
        self.assertTemplateUsed(self.response, "signup.html")
    def test_signup_contains_correct_html(self):
        self.assertContains(self.response, "Sign Up")
    def test_signup_does_not_contain_correct_html(self):
        self.assertNotContains(self.response, "I should not be on the page")
    def test_signup_form(self):
        form = self.response.context.get("form")
        self.assertIsInstance(form, CustomUserCreationForm)
    def test_signup_resolves_correct_view(self):
        view = resolve("/accounts/signup/")
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)
"""

class SignupTests(TestCase):
    username = "testuser"
    email = "testuser@email.com"
    def setUp(self):
        url = reverse("account_signup")
        self.response = self.client.get(url)
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "account/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "I should not be on the page")
    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)