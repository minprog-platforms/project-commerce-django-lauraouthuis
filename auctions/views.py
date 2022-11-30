from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
# from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Category, AuctionListings


def index(request):
    # Check in models.py if an listing (in class AuctionListings is active)
    # proberen of iets als if active_listing == True ook kan
    active_listing = AuctionListings.objects.filter(active_item=True)
    return render(request, "auctions/index.html", {
        "listings": active_listing
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create_listing(request):
    if request.method == "GET":
        # Source for listing all the categories:
        # https://cs50.harvard.edu/web/2020/notes/4/ (Chapter Shell)
        all_categories = Category.objects.all()
        return render(request, "auctions/create_listing.html", {
            "categories": all_categories
        })
    else:
        user = request.user

        # Get the needed data from the form from create_listing.html
        title = request.POST["title"]
        description = request.POST["description"]
        price = request.POST["price"]
        image_url = request.POST["image_url"]
        category = request.POST["category"]

        category_info = Category.objects.get(category_type=category)

        # Create a new lisiting object
        new_listing = AuctionListings(
            title=title,
            description=description,
            image_url=image_url,
            price=float(price),
            category=category_info,
            owner=user
        )

        new_listing.save()  # See source material
        """ waarom reverse index?"""
        return HttpResponseRedirect(reverse(index))


def categories(request):
    return render(request, "auctions/categories.html")
