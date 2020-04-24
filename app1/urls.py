from django.urls import path
from .views import HomePage,AboutPage,ProfilePage

urlpatterns = [
    path('',HomePage.as_view(),name='home'),
    path('about/',AboutPage.as_view(),name='about'),
    path('profile/',ProfilePage.as_view(),name='profile'),

   
]
