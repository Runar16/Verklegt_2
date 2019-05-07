from django.urls import path
from . import views

urlpatterns = [
    path('', views.realtors, name="realtors"),
    path('', views.index, name="users-index"),
    path('realtors/', views.realtors, name="realtors"),
    path('register/', views.register, name='register')
]