from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="frontpage"),
    path('property', views.index, name="property-index"),
]