class ObjectManager:
    def __init__(self):
        self._update_func = None
        self._objects = list()

    def add(self, obj: tuple | list):
        self._objects.append(obj)
        self.update()

    def get(self):
        for obj, group in self._objects:
            yield obj, group

    def group(self, group):
        for obj, gr in self._objects:
            if gr == group:
                yield obj

    def set_update_func(self, func):
        self._update_func = func

    def clear(self):
        self._objects.clear()
        self.update()

    def update(self):
        if self._update_func:
            self._update_func()
