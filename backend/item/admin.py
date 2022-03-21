from django.contrib import admin
from .models import Item

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
  list = ('name', 'price', 'description','short_description', 'image')

  admin.site.register(Item)