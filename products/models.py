from django.db import models


# Models for category

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    cid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254, null=True, blank=True
        )

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


# Models for product

class Product(models.Model):

    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254)
    author = models.CharField(max_length=64)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(
        'Category', related_name='category_product',
        null=True, blank=True, on_delete=models.SET_NULL
    )
    image = models.ImageField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name
        