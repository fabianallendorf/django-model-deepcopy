import copy

from django.db import models


def deepcopy(instance: models.Model, save: bool = False) -> models.Model:
    copied_instance = copy.deepcopy(instance)
    copied_instance.pk = None
    if save:
        copied_instance.save()
    return copied_instance
