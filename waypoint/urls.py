from django.contrib import admin
from django.urls import path
from django.shortcuts import render


# Displays the home page
def home(request):
    context = {
        "greeting": "Welcome to Waypoint"
    }

    return render(
        request,
        "home.html",
        context
    )


# Displays the report form and processes submitted reports
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


# Displays the trail search page
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


# Maps URLs to their views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("report/", report, name="report"),
    path("search/", search, name="search"),
]