
from django.db import models
class Books(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
# Create your models here.
