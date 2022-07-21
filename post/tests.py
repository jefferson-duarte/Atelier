from django.test import TestCase
from model_mommy import mommy


class CreatePostTestCase(TestCase):
    def setUp(self):
        self.titulo = mommy.make('CreatePost')
        
    def test_str(self):
        self.assertEqual(str(self.titulo), self.titulo.titulo)