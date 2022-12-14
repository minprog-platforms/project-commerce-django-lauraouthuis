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


class Bid(models.Model):
    bid = models.FloatField(default=0)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True,
        related_name="user_bid")


class AuctionListings(models.Model):
    """ Pass in everything a listing item needs"""
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=250)
    image_url = models.CharField(max_length=1000)
    price = models.ForeignKey(
        Bid, on_delete=models.CASCADE, blank=True, null=True,
        related_name="user_bid")
    active_item = models.BooleanField(default=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True,
        null=True, related_name="category")
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True,
        null=True, related_name="user")
    watchlist = models.ManyToManyField(
        User, blank=True, null=True, related_name="watchlist")

    def __str__(self):
        """ This function makes sure that the correct titles
        are displayed."""
        return self.title


class Comment(models.Model):
    writer = models.ForeignKey(
        User, on_delete=models.CASCADE,
        blank=True, null=True, related_name="comment_writer")
    listing = models.ForeignKey(
        AuctionListings, on_delete=models.CASCADE,
        blank=True, null=True, related_name="listing_comment")
    message = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.writer} comment on {self.listing}"


""" Personal notes

blank=True -->  One can also add more built-in field validations
                for applying or removing certain constraints on a particular
                field. blank=True will make the field accept blank values.
                It simply means that field can be empty.

on_delete=models.CASCADE -->    if the user gets deleted, the listing gets
                                deleted as well

  """
