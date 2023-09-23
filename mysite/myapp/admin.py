from django.contrib import admin

from .models import Leaning, Product, User


admin.site.register(Product)
admin.site.register(Leaning)
admin.site.register(User)