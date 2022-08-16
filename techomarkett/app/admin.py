from django.contrib import admin

from .models import dataBaseProduct, databaseModel

# Register your models here.
admin.site.register(databaseModel)
admin.site.register(dataBaseProduct)
