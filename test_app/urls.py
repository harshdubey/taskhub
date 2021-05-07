from django.contrib import admin
from django.urls import path
from test_app import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/',views.about, name="about"),
    path('services/', views.services, name="services"),
    path('ourpackages/',views.Our_packages, name="packages"),
    path('contact/', views.contact, name="contact")
]
