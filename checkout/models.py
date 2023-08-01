import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product


class Order(models.Model):
    """
    Create order models
    """
    order_number = models.CharField(
        max_length=32, null=False, editable=False
        )
    full_name = models.CharField(
        max_length=64, null=False, blank=False
        )
    email_address = models.EmailField(
        max_length=254, null=False, blank=False
        )
    mobile_number = models.CharField(
        max_length=32, null=False, blank=False
        )
    street_address1 = models.CharField(
        max_length=80, null=False, blank=False
        )
    street_address2 = models.CharField(
        max_length=80, null=True, blank=True
        )
    city = models.CharField(
        max_length=40, null=False, blank=False
        )
    county = models.CharField(
        max_length=80, null=True, blank=True
        )
    postcode = models.CharField(
        max_length=16, null=True, blank=True
        )
    country = models.CharField(
        max_length=40, null=False, blank=False
        )
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
        )
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
        )
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
        )

    def _generate_order_number(self):
        """
        A random, unique order number can be generated by using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        The grand_total can be updated when a line is added as well as 
        delivery cost
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    The model for web order line item
    """
    order = models.ForeignKey(
        Order, null=False, blank=False, 
        on_delete=models.CASCADE, related_name='lineitems'
        )
    product = models.ForeignKey(
        Product,
        null=False,
        blank=False,
        on_delete=models.CASCADE
        )
    quantity = models.IntegerField(
        null=False,
        blank=False,
        default=0
        )
    lineitem_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False
        )
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)
    def __str__(self):
        return f'Name {self.product.name} on order {self.order.order_number}'
