from django.contrib import admin
from .models import Medical_shop, Stock_availability, General_Medicine, Blood_Bank, Blood_avail

# Register your models here.
admin.site.register(Medical_shop)
admin.site.register(Stock_availability)
admin.site.register(General_Medicine)
admin.site.register(Blood_Bank)
admin.site.register(Blood_avail)
