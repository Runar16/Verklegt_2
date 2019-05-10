from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="frontpage"),
    path('aboutus', views.about_us, name="about_us"),
    path('property', views.index, name="property-index"),
    path('<int:id>', views.get_property_by_id, name="property_details"),
    path('purchase', views.contact_info, name="contact_info"),
    path('payment', views.payment_info, name="payment_info")
]