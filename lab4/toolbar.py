from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout

from styles import BUTTON_STYLE, BIG_FONT


class ToolBar(QWidget):
    def __init__(self, struct):
        super().__init__()

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)

        self._buttons = list()

        for name in struct:
            button = ToolBarItem(name, *struct[name], self._uncheck)
            self._buttons.append(button)
            layout.addWidget(button)

    def _uncheck(self):
        for button in self._buttons:
            button.setChecked(False)


class ToolBarItem(QPushButton):
    def __init__(self, text, clicked, checkable, uncheck):
        super().__init__()

        self.setFont(BIG_FONT)

        self.setStyleSheet(BUTTON_STYLE)
        self.setMinimumWidth(50)
        self.setMinimumHeight(50)

        self.setText(text)
        self.setCheckable(checkable)
        self._clicked_func = clicked
        self._uncheck = uncheck
        self.clicked.connect(self._clicked)

    def _clicked(self):
        if self.isCheckable():
            checked = self.isChecked()
            self._uncheck()
            self.setChecked(checked)
        self._clicked_func()
