from django.test import Client, TestCase
from django.urls import reverse


class WebsiteAboutTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.response = self.client.get(reverse("about"))

    def test_context(self):
        self.assertIsNotNone(self.response.context["committees"])
        self.assertIsNotNone(self.response.context["faq"])


class WebsiteIndexTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.response = self.client.get(reverse("index"))

    def test_context(self):
        self.assertIsNotNone(self.response.context["article_list"])
        self.assertIsNotNone(self.response.context["event_list"])
        self.assertIsNotNone(self.response.context["door_status"])
        self.assertIsNotNone(self.response.context["app_end_date"])
        self.assertIsNotNone(self.response.context["app_start_date"])
        self.assertIsNotNone(self.response.context["is_application"])
        self.assertIsNotNone(self.response.context["index_cards"])
        self.assertIsNotNone(self.response.context["current_date"])
