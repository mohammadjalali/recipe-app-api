from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with email is successful"""
        email = "test@test.com"
        password = "testPass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalized(self):
        """Test the email for the new user is normalized"""
        email = "test@TEST.com"
        user = get_user_model().objects.create_user(
            email=email,
            password='123pass'
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def create_new_superUser(self):
        """Test creating new superUser"""
        user = get_user_model().objects.create_superuser(
            email='test@test.cocm',
            password='test123'
        )

        self.assertTrue(user.is_superUser)
        self.assertTrue(user.is_staff)
