from django.contrib import admin
from django.urls import path, include
from hello import views

urlpatterns = [
    path("",views.index,name="home"),


    #path for the about us page
    path("about",views.about,name = "about"),
    
    #this is the path for the location page
    path("location", views.location, name="location")
]