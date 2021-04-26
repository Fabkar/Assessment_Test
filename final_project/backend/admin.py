from django.contrib import admin
from backend.models import Client, Order, Shipping, Payment


# Register your models here.
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Shipping)
admin.site.register(Payment)