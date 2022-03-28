from django.contrib import admin
from .models import Item
from .models import Category

# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    list = ('name', 'category', 'price', 'description',
            'short_description', 'image', 'created_at')

    admin.site.register(Item)


admin.site.register(Category)
