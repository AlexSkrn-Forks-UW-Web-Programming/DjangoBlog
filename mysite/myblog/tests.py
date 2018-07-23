"""Provide unit tests for myblog app."""

from django.test import TestCase
from django.contrib.auth.models import User
from myblog.models import Post


class PostTestCase(TestCase):
    # Provide base data - Users for our tests
    fixtures = ['myblog_test_fixture.json', ]

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        """Test that Post objects show their titles."""
        expected = "This is a title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)
