from django.db import models

# Create your models here.

class FuturegfList(models.Model):

    Name = models.CharField(max_length=255, null=False, blank=False)
    Age = models.IntegerField()
    Phone = models.CharField(max_length=15, null=True, blank=True)
    Email = models.EmailField()
    Address = models.TextField(max_length=500, null=True, blank=True)
    Image = models.ImageField(upload_to="img/", null=True, blank=True)

    def __str__(self):
        return self.Name




