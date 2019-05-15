from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="realtor"),
    path('<int:id>', views.get_realtor_by_id, name="realtor_details"),
    path('add_property/', views.add_property, name='add_property'),

]