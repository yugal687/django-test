from django.db import models

# Create your models here.
class Todo(models.Model):
   id = models.AutoField(primary_key=True)
   title = models.CharField(max_length=100)
   description = models.TextField()
   completed = models.BooleanField(default=False)

   def _str_(self):
     return self.title