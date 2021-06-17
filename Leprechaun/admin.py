from django.contrib import admin
from .models import Products,payments,Orders,Democlass
# Register your models here.

admin.site.register(Products)
admin.site.register(payments)
admin.site.register(Orders)
admin.site.register(Democlass)

