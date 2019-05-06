from django.urls import path
from . import views

urlpatterns = [
    path('', views.users_index, name="users_index"),
]