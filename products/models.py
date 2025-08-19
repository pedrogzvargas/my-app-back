from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    available_units = models.IntegerField(null=False)
    is_active = models.BooleanField(default=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
