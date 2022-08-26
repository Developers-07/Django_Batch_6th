from django.db import models

# Create your models here.

class Customer(models.Model):

    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=15, null=False, blank=False)
    image = models.ImageField(upload_to="img/Customer/", null=True, blank=True)

    def __str__(self):
        return self.name
