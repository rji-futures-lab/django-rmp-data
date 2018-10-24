"""
Helper functions for working with RMP data models.
"""
from django.apps import apps
from collections import OrderedDict


def get_models(module_name):
    """
    Return all the models with module_name in the import path.
    """
    filtered_models = OrderedDict(
        [
            (k, v) for k, v in apps.get_app_config('rmp').models.items()
            if module_name in str(v)
        ]
    )

    return filtered_models
