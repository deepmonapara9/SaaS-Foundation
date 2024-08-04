from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path("", home_view, name='home'), #index page -> root page
<<<<<<< HEAD
    path("", views.profile_list_view),
    path("<str:username>/", views.profile_detail_view)
=======
    path("<str:username>/", views.profile_view)
>>>>>>> 3a2120fc09fda309b1e2a0621e83501bb5925e6c
]