from django.urls import path
from . import views

app_name = "bloging"

urlpatterns = [
    path("", views.index, name = "index"),
    path("post/<str:slug>", views.detail, name = "detail"),
    path("Fresh_meal_url", views.Fresh_url_view, name = "Fresh_url"),
    path("old_url", views.old_url_redirect, name = "old_url"),
    path("contact", views.contact_view, name="contact"),
    path("about", views.about_view, name="about"),
]