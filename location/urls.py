
from django.urls import path, include
from location import views

urlpatterns = [
    path('hello/', views.hello, name='hello')
    # path('hello/', views.HelloWorldAPIView.as_view(), name='hello_world_api'),

]
