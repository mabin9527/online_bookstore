from django.db import models

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


class Product(models.Model):
    category = models.ForeignKey(
        'Category', related_name='category_product', null=True, blank=True,
        on_delete=models.SET_NULL
        )
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254)
    author = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.FloatField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name