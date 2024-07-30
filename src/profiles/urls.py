from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path("", home_view, name='home'), #index page -> root page
    path("<str:username>/", views.profile_view)
]