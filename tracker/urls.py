# Django best practice: Put all urls in one space/ file ("urls.py")

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),  # Handle 'about/' URL
]
