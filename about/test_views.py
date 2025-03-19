from django.urls import reverse
from django.test import TestCase
from .forms import CollaborateForm
from .models import About, CollaborateRequest


class TestAboutViews(TestCase):

    def setUp(self):
        self.about_content = About(title="About Me", content="This is about me")

        self.about_content.save()

    def test_render_about_me_page_with_collaborate_request_form(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About Me", response.content)
        self.assertIn(b"This is about me", response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)
        
    def test_successful_collaboration_submission(self):
        """Test for submiting collaboration request  form"""
    
        post_data = {
            'name': 'Whon',
            'email': 'whon@test.com',
            'message': 'Can I join?'
        }
        response = self.client.post(reverse(
            'about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request received! I endeavour to respond within 2 working days.',
            response.content
        )