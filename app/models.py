from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User


# class UserProfile(models.Model):
#     # Let us add some simple fields to profile
#     user = models.OneToOneField(User, on_delete=models.PROTECT)
#     city = models.CharField(max_length=100)
#     country = models.CharField(max_length=10)

#     def __unicode__(self):
#         return "%s" % self.user


class DogProduct(models.Model):
    name = models.TextField()
    product_type = models.TextField()
    dog_size = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class Purchase(models.Model):
    dog_product = models.ForeignKey(DogProduct, on_delete=models.PROTECT)
    purchased_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Purchased {self.dog_product} at {self.purchased_at}"


class DogTag(models.Model):
    owner_name = models.TextField()
    dog_name = models.TextField()
    dog_birthday = models.DateField()
