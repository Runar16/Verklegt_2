from django.urls import path
from . import views

urlpatterns = [
    path('', views.properties_index, name="properties_index"),
]