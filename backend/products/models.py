from operator import mod
from tkinter.messagebox import NO
from unittest.util import _MAX_LENGTH
from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2,default=99.99)

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)

    
    def get_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Products):
            return None

        return "112"