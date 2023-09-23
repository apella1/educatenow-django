"""Registering models using django.contrib.admin"""
from django.contrib import admin

# Register your models here.

from .models import Room, Topic, Message


class RoomAdmin(admin.ModelAdmin):
    """_summary_

    Args:
        admin (_type_): _description_
    """

    fieldsets = [
        (
            "Room Information",
            {
                "fields": [
                    "name",
                    "host",
                    "topic",
                ]
            },
        ),
        ("Participants", {"fields": ["participants"]}),
        ("Description", {"fields": ["description"]}),
    ]


class TopicAdmin(admin.ModelAdmin):
    """_summary_

    Args:
        admin (_type_): _description_
    """

    fields = ["name"]


class MessageAdmin(admin.ModelAdmin):
    """_summary_

    Args:
        admin (_type_): _description_
    """

    fieldsets = [("Message Information", {"fields": ["user", "body", "room"]})]


admin.site.register(Room, RoomAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Message, MessageAdmin)
