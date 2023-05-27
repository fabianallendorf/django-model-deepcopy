import copy

from django.db import models


def deepcopy(instance: models.Model) -> models.Model:
    copied_instance = copy.deepcopy(instance)
    copied_instance.pk = None
    return copied_instance
