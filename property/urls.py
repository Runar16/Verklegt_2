from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="frontpage"),
    path('property', views.index, name="property-index"),
    path('<int:id>', views.get_property_by_id, name="property_details"),
    path('purchase', views.customer_info, name="customer_info"),
    path('payment', views.payment_info, name="payment_info")
]