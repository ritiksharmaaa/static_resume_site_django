from django.urls import path 
from . import views 

urlpatterns = [
    path('skill/', views.skill_page , name="skill")
]
