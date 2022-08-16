from distutils.command import upload
from django.db import models

# Create your models here.

class database(models.Model):
    nameNew = models.CharField(max_length=50)
    imgNew = models.ImageField(upload('./static/images'))
    description = models.CharField(max_length=100)
