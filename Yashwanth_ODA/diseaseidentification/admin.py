from django.contrib import admin

# Register your models here.
from diseaseidentification.models import latlng,tips,General_Medicine,Stock_availability,Medical_shop,Blood_Bank,Blood_avail

admin.site.register(latlng)
admin.site.register(tips)
admin.site.register(Medical_shop)
admin.site.register(Stock_availability)
admin.site.register(General_Medicine)
admin.site.register(Blood_Bank)
admin.site.register(Blood_avail)
