from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)   # allow null
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField(default=0)
    brand = models.CharField(max_length=50, null=True, blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)  # safe default

    def __str__(self):
        return self.name
