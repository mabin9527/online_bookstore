from django.contrib import admin
from .models import StaffInfo


class StaffInfoAdmin(admin.ModelAdmin):
    fields = (
        'name', 'age', 'create_time', 'depart', 'gender', 
        'mobile_number', 'street_address1', 'address2', 
        'city', 'county',
    )
    list_display = (
        'name', 'age', 'create_time', 'depart', 'gender', 
        'mobile_number', 'street_address1', 'address2', 
        'city', 'county',
    )
    ordering = ('-create_time',)


admin.site.register(StaffInfo, StaffInfoAdmin)
