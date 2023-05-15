import dataclasses

from django.db import models


@dataclasses.dataclass(frozen=True)
class CopyableModelOptions:
    fields: list[str] = dataclasses.field(default_factory=list)
    exclude: list[str] = dataclasses.field(default_factory=list)


class CopyableModelRegister:
    def __init__(self):
        self._registry = {}

    def register(
        self, model: models.Model, options: CopyableModelOptions | None = None
    ):
        self._registry[model] = options or CopyableModelOptions()

    def unregister(self, model: models.Model):
        del self._registry[model]


register = CopyableModelRegister()
