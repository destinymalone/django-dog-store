from django.contrib import admin
from app import models

# Register your models here.

# admin.site.register(models.UserProfile)
admin.site.register(models.DogProduct)
admin.site.register(models.Purchase)
admin.site.register(models.DogTag)
admin.site.register(models.CatProduct)
admin.site.register(models.CatPurchase)
admin.site.register(models.CatTag)
