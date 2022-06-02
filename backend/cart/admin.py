from django.contrib import admin
from .models import Cart

# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list = ('user', 'item', 'quantity')

    admin.site.register(Cart)



