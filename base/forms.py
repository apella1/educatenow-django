"""Forms"""
from django.forms import ModelForm
from .models import Room, Message


class RoomForm(ModelForm):
    """_summary_

    Args:
        ModelForm (_type_): _description_
    """
    class Meta:
        """_summary_
        """
        model = Room
        fields = "__all__"


class MessageForm(ModelForm):
    """_summary_

    Args:
        ModelForm (_type_): _description_
    """
    class Meta:
        """_summary_
        """
        model = Message
        fields = "__all__"
