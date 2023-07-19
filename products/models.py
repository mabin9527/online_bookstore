from django.db import models

class Category(models.Model):
    db_table = 'bookstore_category'
    cid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254)

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    db_table = 'bookstore_product'
    pid = models.AutoField(primary_key=True)
    category = models.ForeignKey(
        Category, related_name='category_product', on_delete=models.CASCADE
        )
    pdname = models.CharField(max_length=254)
    pdprice = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.FloatField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    description = models.TextField()