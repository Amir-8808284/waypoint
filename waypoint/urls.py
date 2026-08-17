from django.contrib import admin
from django.urls import path
from django.shortcuts import render


def home(request):
    context = {
        "greeting": "Welcome to Waypoint"
    }

    return render(
        request,
        "home.html",
        context
    )


def report(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        trail = request.POST.get("trail", "")
        note = request.POST.get("note", "")

        context = {
            "name": name,
            "email": email,
            "trail": trail,
            "note": note,
        }

        return render(
            request,
            "thank_you.html",
            context
        )

    return render(
        request,
        "report.html"
    )


def search(request):
    query = request.GET.get("q", "")

    context = {
        "query": query
    }

    return render(
        request,
        "search.html",
        context
    )


def catalog(request):
    trails = [
        {
            "name": "Blue Mountain Trail",
            "distance": 8.0,
            "elevation": 300,
            "difficulty": "moderate",
            "is_open": True,
        },
        {
            "name": "Rocky Ridge Route",
            "distance": 12.5,
            "elevation": 650,
            "difficulty": "hard",
            "is_open": True,
        },
        {
            "name": "River Run",
            "distance": 6.2,
            "elevation": 150,
            "difficulty": "easy",
            "is_open": True,
        },
        {
            "name": "Forest Loop",
            "distance": 9.8,
            "elevation": 400,
            "difficulty": "moderate",
            "is_open": False,
        },
        {
            "name": "Summit Challenge",
            "distance": 15.4,
            "elevation": 900,
            "difficulty": "expert",
            "is_open": True,
        },
        {
            "name": "Lake View Trail",
            "distance": 5.7,
            "elevation": 200,
            "difficulty": "easy",
            "is_open": True,
        },
    ]

    context = {
        "trails": trails
    }

    return render(
        request,
        "catalog.html",
        context
    )


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("report/", report, name="report"),
    path("search/", search, name="search"),
    path("catalog/", catalog, name="catalog"),
]