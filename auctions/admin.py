from django.contrib import admin
# Import the classes that you made in models.py
from .models import User, Category, AuctionListings, Bids, Comments

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(AuctionListings)
admin.site.register(Bids)
admin.site.register(Comments)
