import copy

from django.db import models

from django_model_deepcopy.register import register


def deepcopy(instance: models.Model, **override) -> models.Model:
    if not register.is_registered(instance.__class__):
        raise ValueError(f"Model '{instance.__class__}' is not registered")

    options = register.get_options(instance.__class__)
    copied_instance = copy.deepcopy(instance)
    copied_instance.pk = None
    for field_name, value in override.items():
        setattr(copied_instance, field_name, value)
    for field in options.fields:
        if field.one_to_one or field.many_to_one:
            related_object = getattr(instance, field.name)
            if related_object is None or not register.is_registered(related_object.__class__):
                continue
            copied_related_object = deepcopy(related_object)
            setattr(copied_instance, field.name, copied_related_object)
        elif field.many_to_many or field.one_to_many:
            if not register.is_registered(field.related_model):
                continue
            related_manager = getattr(instance, field.name)
            copied_related_objects = [deepcopy(o) for o in related_manager.all()]
            related_manager.set(copied_related_objects)
    copied_instance.save()
    return copied_instance
