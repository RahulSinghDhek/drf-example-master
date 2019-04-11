import django.contrib.auth
from django.db import models
from django.conf import settings

class Profile(models.Model):
    display_name = models.CharField(max_length=255)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)

class Listing(models.Model):
    title = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, related_name='listings', null=True,on_delete=models.CASCADE)
    owners = models.ManyToManyField(
        Profile,
        related_name='owned_listings',
        db_table='profile_listing',
        blank=True
    )
