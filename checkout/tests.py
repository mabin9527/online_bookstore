from django.test import TestCase
from django.contrib.messages import get_messages
from django.contrib.auth.models import User

from checkout.models import Order
from profiles.models import UserProfile


class TestCheckoutViews(TestCase):
    def setUp(self):
        """
        Create test users, regular, and superuser and a test order
        """
        test_user = User.objects.create_user(
            username='test_user', password='test_password')
        test_user_superuser = User.objects.create_superuser(
            username='test_user_superuser', password='test_password')

        test_user.save()
        test_user_superuser.save()
        test_user = UserProfile.objects.get(user=test_user)

        Order.objects.create(
            full_name='Test Name',
            email_address='admin@gmail.com',
            mobile_number='0889791391',
            street_address1='Test Address',
            street_address2='Test Address2',
            city='Dublin',
            county='Dublin',
            country='Ireland',
        )

    def tearDown(self):
        """
        Delete test orders
        """
        Order.objects.all().delete()

    def test_checkout_view_empty_cart(self):
        """
        This test test an empty cart for checkout and verifies
        """
        response = self.client.get('/checkout/')
        self.assertRedirects(response, '/products/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), "There's nothing in your basket at the moment")
