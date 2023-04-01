from PyQt5.QtWidgets import QLineEdit


class InputWidget(QLineEdit):
    Base = 0
    Int = 10
    Natural = 11
    Float = 20
    PositiveFloat = 21
    Function = 30

    def __init__(self, parent=None, __type=Base, default=''):
        if parent:
            super().__init__(parent)
        else:
            super().__init__()

        self.finished = None

        font = self.font()
        font.setPointSize(16)
        self.setFont(font)

        self.__type = __type
        self.textChanged.connect(self.text_changed)
        self.editingFinished.connect(self.editing_finished)

        self.setText(default)

    def connect(self, func):
        if func:
            self.finished = func
            self.editing_finished()
        return self

    def editing_finished(self):
        if not self.finished:
            return
        if self.__type in (InputWidget.Int, InputWidget.Natural):
            try:
                x = int(self.text())
            except:
                self.finished('Error')
            else:
                self.finished(x)
        elif self.__type in (InputWidget.Float, InputWidget.PositiveFloat):
            try:
                x = float(self.text())
            except:
                self.finished('Error')
            else:
                self.finished(x)
        else:
            self.finished(self.text())

    def text_changed(self):
        if self.__type in (InputWidget.Base, InputWidget.Int, InputWidget.Function):
            return
        modified_text = list()
        if self.__type == InputWidget.Natural:
            self.natural_filter(self.text(), modified_text)
        elif self.__type == InputWidget.PositiveFloat:
            self.positive_float_filter(self.text(), modified_text)
        elif self.__type == InputWidget.Float:
            text = self.text()
            if text and text[0] == '-':
                self.positive_float_filter(text[1:], modified_text)
                modified_text.insert(0, '-')
            else:
                self.positive_float_filter(text, modified_text)
        self.setText(''.join(modified_text))

    @staticmethod
    def natural_filter(text, output):
        can_place_zero = False
        for sym in text:
            if sym.isdigit() and sym != '0':
                can_place_zero = True
                output.append(sym)
            elif sym == '0' and can_place_zero:
                output.append(sym)

    @staticmethod
    def positive_float_filter(text, output):
        num_start = True
        can_place_zero = True
        can_place_dot = True
        for sym in text:
            if sym == '0' and can_place_zero:
                output.append(sym)
                if num_start:
                    can_place_zero = False
            elif sym in '.,' and can_place_dot:
                if not output:
                    output.append('0')
                output.append('.')
                can_place_zero = True
                can_place_dot = False
            elif sym.isdigit() and sym != '0':
                if not can_place_zero:
                    output.pop(0)
                output.append(sym)
                can_place_zero = True
            num_start = False
