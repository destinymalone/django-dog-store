from django.contrib import admin
from app import models

# Register your models here.

# admin.site.register(models.UserProfile)
admin.site.register(models.DogProduct)
admin.site.register(models.Purchase)
admin.site.register(models.DogTag)
