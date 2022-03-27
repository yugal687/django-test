from datetime import datetime
from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
  
    def __str__(self):
        return self.name


# Create your models here
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    price = models.IntegerField()
    description = models.TextField()
    short_description = models.TextField(max_length=140, default='SOME STRING')
    image = models.ImageField(null=True, blank=True, upload_to='static/images')

    def _str_(self):
        return self.name
