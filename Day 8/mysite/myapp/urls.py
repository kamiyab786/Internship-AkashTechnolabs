from django.urls import path
from . import views

urlpatterns = [
    path('', views.travel, name='travel'),
    path('services', views.services, name='services'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]
