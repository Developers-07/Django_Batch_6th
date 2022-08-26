from django.db import models

# Create your models here.

class Profile(models.Model):

    name = models.CharField(max_length=100, null=False, blank=False)
    address = models.TextField(max_length=1000, null=True, blank=True)
    email = models.EmailField()
    phn = models.IntegerField()

    def __str__(self):
        return self.name
