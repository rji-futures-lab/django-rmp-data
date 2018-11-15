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


def get_model_by_source_file(source_file_name):
    """
    Return a Django model class to which source_file_name is mapped.

    If none found, return None.
    """
    lookup = dict([
        (getattr(i, 'source_file', i._meta.object_name), i)
        for i in apps.get_app_config('rmp').models.values()
    ])
    try:
        model = lookup[source_file_name]
    except KeyError:
        model = None

    return model
