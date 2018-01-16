from django.test import TestCase

# Create your tests here.

class Test(TestCase):
    def test_self(self):
        self.assertEqual(2*2,4)
