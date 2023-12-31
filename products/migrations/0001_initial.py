# Generated by Django 3.2.20 on 2023-07-19 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('pdname', models.CharField(max_length=254)),
                ('pdprice', models.DecimalField(decimal_places=2, max_digits=6)),
                ('discount', models.FloatField()),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_product', to='products.category')),
            ],
        ),
    ]
