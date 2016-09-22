from django.contrib import admin
from .models import Customer, Brand, Item, Order

admin.site.register(Customer)
admin.site.register(Brand)
admin.site.register(Item)
admin.site.register(Order)
