
from django.urls import path
from . import views
urlpatterns = [
path("service/", views.services_page , name="services" ),
]
