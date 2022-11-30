"""This file is where you will define any models for
your web application, where each model represents
some type of data you want to store in your database."""

from django.contrib.auth.models import AbstractUser
from django.db import models

"""Remember that each time you change anything in auctions/models.py
you'll need to first run python3 manage.py makemigrations and then
python manage.py migrate to migrate those changes to your database"""

""" The application should have at least three models in addition to the User
model: auction listings, bids and comments."""


class User(AbstractUser):
    pass


class Category(models.Model):
    """Class to the define the category a listing belongs to """
    category_type = models.CharField(max_length=64)

    def __str__(self):
        """ This function makes sure that in the admin panel the
        name of the category is displayed, rather than 'Category
        object(1), etc."""
        return self.category_type


class AuctionListings(models.Model):
    """ Pass in everything a listing needs"""
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=250)
    image_url = models.CharField(max_length=1000)
    price = models.FloatField(default=0.0)
    active_item = models.BooleanField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True,
        null=True, related_name="user")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE,
    # blank=True, null=True, related_name="user")

    def __str__(self):
        """ This function makes sure that in the admin panel the
        name of the category is displayed, rather than 'Category
        object(1), etc."""
        return self.title


class Bids(models.Model):
    pass


class Comments(models.Model):
    pass


""" Personal notes
  ???? why use models.Model in the class parameters?

blank=True -->  One can also add more built-in field validations
                for applying or removing certain constraints on a particular
                field. blank=True will make the field accept blank values.
                It simply means that field can be empty.

on_delete=models.CASCADE -->    if the user gets deleted, the listing gets
                                deleted as well

  """
