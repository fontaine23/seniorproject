from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('home.html', views.home, name="home"),
	path('highlights.html', views.highlights, name="highlights"),
	path('gallery.html', views.gallery, name="gallery"),
	path('contact.html', views.contact, name="contact"),
   
]