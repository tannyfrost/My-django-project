from django import views
from django.urls import path
from website import views


urlpatterns = [
    path('', views.index),
    path('home/', views.home, name='home'),   
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
]