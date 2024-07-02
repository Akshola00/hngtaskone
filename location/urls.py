
from django.urls import path, include
from location import views

urlpatterns = [
    path('hello', views.hello, name='hello')
]
