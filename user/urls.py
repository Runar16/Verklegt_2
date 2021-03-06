from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="users-index"),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit/', views.edit_profile, name="edit_profile"),
    path('cart/', views.cart, name="cart"),
    path('favourite/', views.favourite, name="favourite"),
    url(r'^password/$', views.change_password, name='change_password'),
]
