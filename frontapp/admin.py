from django.contrib import admin

# Register your models here.
from .models import User, Product, Blog

admin.site.register(Product)
admin.site.register(User)
admin.site.register(Blog)
