from django.core.exceptions import FieldDoesNotExist
from django.db import models


def has_field(model: type[models.Model], field_name: str) -> bool:
    try:
        model._meta.get_field(field_name)
        return True
    except FieldDoesNotExist:
        return False
