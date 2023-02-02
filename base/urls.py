from django.urls import path
from . import views

# adding dynamic routing to the room view

urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
]