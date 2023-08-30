"""
Registered apps
"""
from django.apps import AppConfig


class BaseConfig(AppConfig):
    """_summary_

    Args:
        AppConfig (_type_): _description_
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
