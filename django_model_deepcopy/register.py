class CopyableModelRegister:
    def __init__(self):
        self._registry = {}

    def register(self, model):
        self._registry[model] = {}

    def unregister(self, model):
        del self._registry[model]

register = CopyableModelRegister()