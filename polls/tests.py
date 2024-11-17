from django.test import SimpleTestCase
from django.urls import resolve, reverse

from .views import HomePageView, AboutPageView

class HomePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)
        
    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)
    def test_homepage_uses_correct_template(self):
        self.assertTemplateUsed(self.response, "home.html")
    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "Home")
    def test_homepage_does_not_contain_correct_html(self):
        self.assertNotContains(self.response, "I should not be on the page.")
    def test_homepage_url_resolves_correct_view(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
        
class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("about")
        self.response = self.client.get(url)
    def test_about_status_code(self):
        self.assertEqual(self.response.status_code, 200)
    def test_about_correct_template(self):
        self.assertTemplateUsed(self.response, "about.html")
    def test_about_correct_html(self):
        self.assertContains(self.response, "About")
    def test_about_incorrect_html(self):
        self.assertNotContains(self.response, "I should not be on the page")
    def test_about_resolves_correct_view(self):
        view = resolve("/about/")
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)