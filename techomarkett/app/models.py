from django.db import models

# Create your models here.
class databaseModel(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class dataBaseProduct(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    new = models.BooleanField()
    brand = models.ForeignKey(databaseModel,on_delete=models.PROTECT)
    fecha = models.DateTimeField()


    def __str__(self):
        return self.nombre