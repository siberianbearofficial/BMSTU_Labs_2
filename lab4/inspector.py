from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidget, QListWidgetItem

from styles import LIST_STYLE


class Inspector(QListWidget):
    def __init__(self, select_func=None, remove_func=None, edit_func=None):
        super().__init__()

        self.setStyleSheet(LIST_STYLE)

        if select_func:
            self.currentItemChanged.connect(select_func)
            self.doubleClicked.connect(edit_func)
        self._remove_func = remove_func
        self._edit_func = edit_func

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Delete and self._remove_func:
            self._remove_func()
        elif e.key() == Qt.Key_Space and self._edit_func:
            self._edit_func()
        else:
            super().keyPressEvent(e)

    def update_items(self, get_objects):
        current_row = self.currentRow()
        self.clear()
        for obj, _ in get_objects:
            self.addItem(InspectorItem(str(obj), id(obj)))
        current_row = max(0, min(current_row, self.count()))
        self.setCurrentRow(current_row)


class InspectorItem(QListWidgetItem):
    def __init__(self, text, _id):
        super().__init__()
        self.setText(text)
        self.id = _id
