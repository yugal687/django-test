from django.db import models

# Create your models here.
class Item(models.Model):
   name = models.CharField(max_length=100)
   price = models.IntegerField()
   description = models.TextField()
   short_description = models.TextField(max_length=140, default='SOME STRING')
   image = models.ImageField(null=True, blank= True, upload_to='static/images')

   def _str_(self):
     return self.name