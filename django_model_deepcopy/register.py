import dataclasses

from django.db import models

from django_model_deepcopy import model_helper


@dataclasses.dataclass(frozen=True)
class CopyableModelOptions:
    fields: list[models.Field] = dataclasses.field(default_factory=list)
    exclude: list[models.Field] = dataclasses.field(default_factory=list)


class CopyableModelRegister:
    def __init__(self):
        self._registry: dict[type[models.Model], CopyableModelOptions] = {}

    def register(self, model: type[models.Model], options: CopyableModelOptions | None = None):
        if options is not None:
            RegisterValidator.validate_options(model, options)
            self._registry[model] = options
        else:
            fields = self._get_all_model_fields(model)
            self._registry[model] = CopyableModelOptions(fields=fields, exclude=[])

    def unregister(self, model: type[models.Model]):
        del self._registry[model]

    def is_registered(self, model: type[models.Model]) -> bool:
        return model in self._registry

    def get_options(self, model: type[models.Model]) -> CopyableModelOptions:
        return self._registry[model]

    @staticmethod
    def _get_all_model_fields(model: type[models.Model]) -> list[models.Field]:
        return model._meta.get_fields(include_parents=True, include_hidden=True)


class RegisterValidator:
    @staticmethod
    def validate_options(model: type[models.Model], options: CopyableModelOptions):
        for field in options.fields + options.exclude:
            if not model_helper.has_field(model, field):
                raise ValueError(f"Model '{model}' does not have field '{field}'")


register = CopyableModelRegister()
