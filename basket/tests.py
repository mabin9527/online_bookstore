from django.contrib.messages import get_messages
from django.urls import reverse
from django.test import TestCase

from products.models import Product, Category


class TestViews(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            name='Test Product',
            category=self.category,
            price=36.99
        )

    def tearDown(self):
        self.product.delete()
        self.category.delete()

    def test_view_basket_view(self):
        url = reverse('view_basket')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket/basket.html')

