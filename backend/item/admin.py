from django.contrib import admin
from .models import Item

# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    list = ('name', 'category', 'price', 'description',
            'short_description', 'image', 'created_at')

    admin.site.register(Item)
