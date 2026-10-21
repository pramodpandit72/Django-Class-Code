from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class URLTest(TestCase):
    def test_sampletest(self):
        response = self.client.get('/sampletest/')
        self.assertEqual(response.status_code, 200)

    def test_sampletest_content(self):
        response = self.client.get('/sampletest/')
        self.assertContains(response, 'This is a sample test page')

    def test_sampletest_negativeurl(self):
        response = self.client.get('/newsampletest/')
        self.assertEqual(response.status_code, 404)

    def test_sampletest_urlname(self):
        url = reverse('st')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_sampletest_parameter(self):
        url = reverse('st1', args = [23])
        response = self.client.get(url)
        self.assertContains(response, 23)
        self.assertNotContains(response, 25)

    def test_home_template(self):
        response = self.client.get('/home/')
        self.assertTemplateUsed(response, 'home.html')

    def test_old_redirect(self):
        response = self.client.get('/old/')
        self.assertRedirects(response, '/new/')
