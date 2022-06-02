from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    # @staticmethod
    # def categories():
    #     return Category.objects.all()
  
    def __str__(self):
        return self.name


# Create your models here
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='items', null=True )
    price = models.IntegerField()
    description = models.TextField()
    short_description = models.TextField(max_length=140, default='Description', null=True)
    image = models.ImageField(null=True, blank=True, upload_to='static/images')

    def _str_(self):
        return self.name

