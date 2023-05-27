import dataclasses

from django.db import models

from django_model_deepcopy import model_helper


@dataclasses.dataclass(frozen=True)
class CopyableModelOptions:
    fields: list[str] = dataclasses.field(default_factory=list)
    exclude: list[str] = dataclasses.field(default_factory=list)


class CopyableModelRegister:
    def __init__(self):
        self._registry: dict[type[models.Model], CopyableModelOptions] = {}

    def register(self, model: type[models.Model], options: CopyableModelOptions | None = None):
        if options is not None:
            RegisterValidator.validate_options(model, options)
        self._registry[model] = options or CopyableModelOptions()

    def unregister(self, model: type[models.Model]):
        del self._registry[model]


class RegisterValidator:
    @staticmethod
    def validate_options(model: type[models.Model], options: CopyableModelOptions):
        for field in options.fields + options.exclude:
            if not model_helper.has_field(model, field):
                raise ValueError(f"Model '{model}' does not have field '{field}'")


register = CopyableModelRegister()
