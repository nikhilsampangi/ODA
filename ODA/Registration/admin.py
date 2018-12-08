from django.contrib import admin

# Register your models here.
from .models import Medical,Stock
admin.site.register(Medical)
admin.site.register(Stock)