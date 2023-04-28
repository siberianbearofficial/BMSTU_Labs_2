from PyQt5.QtGui import QColor

from random import randint


class Color(QColor):
    def __init__(self, red, green=None, blue=None, alpha=None):
        if isinstance(red, str):
            if '#' in red:
                super().__init__(red.strip())
            else:
                color = list()
                for col in red.strip().split():
                    new_col = list()
                    for el in col:
                        if el.isdigit() or el in '.,':
                            new_col.append(el.replace(',', '.'))
                    color.append(min(int(float(''.join(new_col))), 255))
                super().__init__(*color)
        elif red is not None and green is not None and blue is not None:
            red, green, blue = int(float(red)), int(float(green)), int(float(blue))
            if alpha:
                super().__init__(red, green, blue, alpha)
            else:
                super().__init__(red, green, blue)
        elif isinstance(red, QColor):
            super().__init__(red)
        else:
            raise ValueError(f'Oops, invalid color format: {red}, {green}, {blue}, {alpha}!')

    def __str__(self):
        return f'rgba({self.red()}, {self.green()}, {self.blue()}, {self.alpha()})'

    @staticmethod
    def random():
        red = randint(20, 240)
        green = randint(20, 240)
        blue = randint(20, min(570 - red - green, 240))
        return Color(red, green, blue)


BG_COLOR = Color(255, 255, 255)
BLACK_COLOR = Color(0, 0, 0)
RED_COLOR = Color(255, 0, 0)
BLUE_COLOR = Color(0, 0, 255)
SELECTED_COLOR = Color(130, 80, 190)
