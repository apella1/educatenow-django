"""
Base url patterns
"""
from django.urls import path
from . import views

# adding dynamic routing to the room view

urlpatterns = [
    path("login", views.login_view, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("register", views.register_user, name="register"),
    path("", views.home, name="home"),
    path("room/<str:pk>/", views.room_view, name="room"),
    path("user-profile/<str:pk>/", views.user_profile, name="user-profile"),
    path("create-room", views.create_room, name="create-room"),
    path("update-room/<str:pk>/", views.update_room, name="update-room"),
    path("delete-room/<str:pk>/", views.delete_room, name="delete-room"),
    path("update-message/<str:pk>/", views.update_message, name="update-message"),
    path("delete-message/<str:pk>/", views.delete_message, name="delete-message"),
]
