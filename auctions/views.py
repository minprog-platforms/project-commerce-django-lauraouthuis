from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
# from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Category, AuctionListings, Comment, Bid


def index(request):
    # Check in models.py if an listing (in class AuctionListings is active)
    # proberen of iets als if active_listing == True ook kan
    if request.method == "POST":
        categoryFromForm = request.POST['category']
        category = Category.objects.get(category_type=categoryFromForm)
        active_listing = AuctionListings.objects.filter(
            active_item=True, category=category)
    else:
        active_listing = AuctionListings.objects.filter(active_item=True)
    all_categories = Category.objects.all()
    return render(request, "auctions/index.html", {
        "listings": active_listing,
        "categories": all_categories,
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
        # user_larry = current_user
        user_larry = request.user

        # Get the needed data from the form from create_listing.html
        title = request.POST["title"]
        description = request.POST["description"]
        price = request.POST["price"]
        image_url = request.POST["image_url"]
        category = request.POST["category"]

        category_info = Category.objects.get(category_type=category)

        # Bidding item
        bid = Bid(bid=float(price), user=user_larry)
        bid.save()

        # Create a new lisiting object
        new_listing = AuctionListings(
            title=title,
            description=description,
            image_url=image_url,
            price=bid,
            category=category_info,
            owner=user_larry
        )

        new_listing.save()  # See source material
        return HttpResponseRedirect(reverse(index))


def show_category(request):
    # Make sure that if a user selects a category, the user gets redirected
    # to the page with items of just that category
    if request.method == "POST":
        categoryFromForm = request.POST['category']
        category = Category.objects.get(category_type=categoryFromForm)
        active_listings = AuctionListings.objects.filter(
            active_item=True, category=category)
        all_categories = Category.objects.all()
        return render(request, "auctions/categories.html", {
            "listings": active_listings,
            "categories": all_categories
        })


def listing(request, id):
    listing_info = AuctionListings.objects.get(pk=id)
    listing_in_watchlist = request.user in listing_info.watchlist.all()
    all_comments = Comment.objects.filter(listing=listing_info)
    is_owner = request.user.username == listing_info.owner.username

    return render(request, "auctions/listing.html", {
        "listing": listing_info,
        "listing_in_watchlist": listing_in_watchlist,
        "all_comments": all_comments,
        "is_owner": is_owner,
    })


def remove_from_watchlist(request, id):
    listing_info = AuctionListings.objects.get(pk=id)
    user_larry = request.user
    listing_info.watchlist.remove(user_larry)
    return HttpResponseRedirect(reverse("listing", args=(id, )))


def add_to_watchlist(request, id):
    listing_info = AuctionListings.objects.get(pk=id)
    user_larry = request.user
    listing_info.watchlist.add(user_larry)
    return HttpResponseRedirect(reverse("listing", args=(id, )))


def display_watchlist(request):
    user_larry = request.user
    listings = user_larry.watchlist.all()
    return render(request, "auctions/watchlist.html", {
        "listings": listings
    })


def add_comment(request, id):
    user_larry = request.user
    listing_info = AuctionListings.objects.get(pk=id)
    message = request.POST["add_comment"]

    new_comment = Comment(
        writer=user_larry,
        listing=listing_info,
        message=message
    )

    new_comment.save()

    return HttpResponseRedirect(reverse("listing", args=(id, )))


def add_bid(request, id):
    new_bid = float(request.POST['new_bid'])
    listing_info = AuctionListings.objects.get(pk=id)
    listing_in_watchlist = request.user in listing_info.watchlist.all()
    all_comments = Comment.objects.filter(listing=listing_info)
    is_owner = request.user.username == listing_info.owner.username
    if new_bid > listing_info.price.bid:
        update_bid = Bid(user=request.user, bid=new_bid)
        update_bid.save()
        listing_info.price = update_bid
        listing_info.save()
        return render(request, "auctions/listing.html", {
            "listing": listing_info,
            "message": "Bid is accepted",
            "update": True,
            "listing_in_watchlist": listing_in_watchlist,
            "all_comments": all_comments,
            "is_owner": is_owner,
        })
    else:
        return render(request, "auctions/listing.html", {
            "listing": listing_info,
            "message": "Bid denied",
            "update": False,
            "listing_in_watchlist": listing_in_watchlist,
            "all_comments": all_comments,
            "is_owner": is_owner,
        })


def close_auction(request, id):
    listing_info = AuctionListings.objects.get(pk=id)
    listing_info.active_item = False
    listing_info.save()
    is_owner = request.user.username == listing_info.owner.username
    all_comments = Comment.objects.filter(listing=listing_info)
    listing_in_watchlist = request.user in listing_info.watchlist.all()
    return render(request, "auctions/listing.html", {
        "listing": listing_info,
        "listing_in_watchlist": listing_in_watchlist,
        "all_comments": all_comments,
        "is_owner": is_owner,
        "update": True,
        "message": "Auction closed!"
    })
