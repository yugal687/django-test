from django.db import models

# Create your models here.
class Item(models.Model):
   name = models.CharField(max_length=100)
   price = models.IntegerField()
   description = models.TextField()
   image = models.ImageField(null=True, blank= True, upload_to='static/images')

   def _str_(self):
     return self.name