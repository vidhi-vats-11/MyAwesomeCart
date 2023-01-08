from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('about', views.about, name="aboutUs"),
    path('contact', views.contact, name="TrackingStatus"),
    path('tracker', views.tracker, name="ShopHome"),
    path('search', views.search, name="search"),
    path('prodView', views.prodView, name="search"),
    path('checkout', views.checkout, name="Checkout"),
]


# http://127.0.0.1:3000/shop/