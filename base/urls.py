from django.urls import path
from . import views

# adding dynamic routing to the room view

urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room_view, name='room'),
    path('create-room', views.create_room, name='create-room'),
    path('update-room/<str:pk>/', views.update_room, name='update-room'),
    path('delete-rodom/<str:pk>/', views.delete_room, name='delete-room'),
]