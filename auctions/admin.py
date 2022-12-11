from django.contrib import admin
# Import the classes that you made in models.py
from .models import User, Category, AuctionListings, Bid, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(AuctionListings)
admin.site.register(Bid)
admin.site.register(Comment)
