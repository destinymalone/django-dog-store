from django.db import models
from django.utils import timezone


class DogProduct(models.Model):
    name = models.TextField()
    product_type = models.TextField()
    dog_size = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class DogTag(models.Model):
    owner_name = models.TextField()
    dog_name = models.TextField()
    dog_birthday = models.DateField()


class Purchase(models.Model):
    dog_product = models.ForeignKey(DogProduct, on_delete=models.PROTECT)
    purchased_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Purchased {self.dog_product} at {self.purchased_at}"


class CatProduct(models.Model):
    name = models.TextField()
    product_type = models.TextField()
    cat_size = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class CatTag(models.Model):
    owner_name = models.TextField()
    cat_name = models.TextField()
    cat_birthday = models.DateField()


class CatPurchase(models.Model):
    cat_product = models.ForeignKey(CatProduct, on_delete=models.PROTECT)
    purchased_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Purchased {self.cat_product} at {self.purchased_at}"
