class ObjectManager:
    def __init__(self):
        self._update_funcs = None
        self._objects = list()
        self.selected = None

    def add(self, obj: tuple | list):
        self._objects.append(obj)
        self.select(id(obj[0]))

    def get(self, _id=None, selected=None, every=None):
        if selected:
            yield self._get_by_id(self.selected)
        elif _id is not None:
            yield self._get_by_id(_id)
        else:
            for obj, group in self._objects:
                if every or not self.is_selected(obj):
                    yield obj, group

    def edit(self, struct, obj=None):
        if obj is None:
            obj = self._get_by_id(self.selected)[0]
        for field, val in struct:
            obj.__dict__[field] = val if val is not None else 0
        self.update()

    def is_selected(self, obj):
        return id(obj) == self.selected

    def _get_by_id(self, _id):
        for obj, group in self._objects:
            if id(obj) == _id:
                return obj, group
        return None, None

    def group(self, group):
        for obj, gr in self._objects:
            if gr == group:
                yield obj

    def select(self, _id=None):
        """
        Function that selects the object by id.
        :param _id: object id
        :return:
        """

        if _id == self.selected:
            return

        self.selected = _id
        self.update()

    def remove(self, _id=None):
        if _id is not None:
            self._remove_by_id(_id)
        elif self.selected is not None:
            self._remove_by_id(self.selected)
        self.update()

    def _remove_by_id(self, _id):
        if (obj := self._get_by_id(_id)) is not None and obj in self._objects:
            self._objects.remove(obj)

    def set_update_funcs(self, *funcs):
        self._update_funcs = funcs
        return self

    def clear(self, group=None):
        if group is None:
            self._objects.clear()
        else:
            for obj, gr in self._objects:
                if gr == group:
                    self._objects.remove((obj, gr))

        self.update()

    def update(self):
        if self._update_funcs:
            for func in self._update_funcs:
                func()
