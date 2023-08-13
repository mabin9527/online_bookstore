from django.db import models

# Models for employee 


class StaffInfo(models.Model):
    name = models.CharField(max_length=16)
    age = models.IntegerField(verbose_name='age')
    create_time = models.DateField(verbose_name='Hire Date')
    depart = models.CharField(max_length=64, verbose_name='Department')
    mobile_number = models.CharField(
        max_length=32, null=True, blank=True
    )
    street_address1 = models.CharField(
        max_length=80, null=True, blank=True
    )
    address2 = models.CharField(
        max_length=80, null=True, blank=True
    )
    city = models.CharField(
        max_length=40, null=True, blank=True
    )
    county = models.CharField(
        max_length=80, null=True, blank=True
    )
    gender_choices = (
        (1, 'Male'),
        (2, 'Female'),
    )
    gender = models.SmallIntegerField(choices=gender_choices)

