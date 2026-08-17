from django.urls import path

from . import views


app_name = "trails"


urlpatterns = [
    path("", views.catalog, name="catalog"),
]