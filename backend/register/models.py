from django.db import models

# Create your models here.
class Register(models.Model):
   username = models.CharField(max_length=100)
   email = models.EmailField()
   password1 = models.TextField()
   password2 = models.TextField()
   

   def _str_(self):
     return self.username