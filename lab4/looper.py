from PyQt5.QtCore import QThread, pyqtSignal


class Looper(QThread):
    step = pyqtSignal(object)

    def __init__(self, func):
        super().__init__()
        self.func = func

    def run(self):
        if self.func:
            for obj in self.func():
                self.step.emit(obj)
