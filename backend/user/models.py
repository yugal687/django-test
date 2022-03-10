from django.db import models

# Create your models here.
class User(models.Model):
   name = models.CharField(max_length=100)
   address = models.CharField(max_length=100)
   designation = models.CharField(max_length=100)
   contact = models.CharField(max_length=100)

   def _str_(self):
     return self.name