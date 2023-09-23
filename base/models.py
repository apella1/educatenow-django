"""
Base models
"""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    """Topic model

    Args:
        models (_type_): _description_
    """

    objects = models.Manager()
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return str(self.name)


class Room(models.Model):
    """Room model

    Args:
        models (_type_): _description_

    """

    objects = models.Manager()
    name = models.CharField(max_length=200, unique=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=False)
    participants = models.ManyToManyField(User, related_name="participants", blank=True)
    description = models.TextField(null=False, blank=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """_summary_"""

        ordering = ["-updated", "-created"]

    def __str__(self):
        return str(self.name)


class Message(models.Model):
    """_summary_

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """

    objects = models.Manager()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # creating a many-to-one relationship with Room
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """_summary_"""

        ordering = ["-updated", "-created"]

    def __str__(self):
        return str(self.body[0:50])
