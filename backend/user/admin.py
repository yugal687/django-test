from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
  list = ('name', 'address', 'designation', 'contact')

  admin.site.register(User)