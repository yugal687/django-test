from django.db import models
from item.models import Item
from user.models import User

# Create your models here.
class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    # user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user} - {self.item} - {self.quantity}"