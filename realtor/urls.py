from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="realtor"),
    path('<int:id>', views.get_realtor_by_id, name="realtor_details")

]