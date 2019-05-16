from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="realtor"),
    path('<int:id>', views.get_realtor_by_id, name="realtor_details"),
    path('add_property/', views.add_property, name='add_property'),
    path('change_property/<int:id>', views.change_property, name='change_property'),
    path('my_properties', views.my_properties, name='my_properties'),
    path('orders', views.get_all_orders, name='orders')
]
