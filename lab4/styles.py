from PyQt5.QtGui import QFont

from color import *

BUTTON_STYLE = (f'QPushButton {{'
                f'background-color: {WIDGET_BG_COLOR};'
                f'border-radius: 10px;'
                f'color: {BLACK_COLOR};'
                f'}}'
                f'QPushButton::checked {{'
                f'background-color: {ACCENT_COLOR};'
                f'}}'
                f'QPushButton::hover {{'
                f'background-color: {WHITE_COLOR};'
                f'}}'
                f'QPushButton::disabled {{'
                f'color: {DARK_COLOR};'
                f'background-color: {WHITE_COLOR};'
                f'}}')

LIST_STYLE = (f'QListWidget {{'
              f'background-color: {WIDGET_BG_COLOR};'
              f'border-radius: 10px;'
              f'padding: 10px;'
              f'}}'
              f'QListWidget::item {{'
              f'background-color: {WIDGET_BG_COLOR};'
              f'padding-top: 5px;'
              f'padding-bottom: 5px;'
              f'}}'
              f'QListWidget::item::selected {{'
              f'color: {SELECTED_COLOR};'
              f'}}'
              f'QListWidget::item::hover {{'
              f'color: {DARK_COLOR};'
              f'}}'
              f'QListWidget QScrollBar {{'
              f'height: 0px;'
              f'width: 0px;'
              f'}}')

LIST_ITEM_STYLE = (f'QListWidgetItem {{'
                   f''
                   f'}}')

COMBO_BOX_STYLE = (f'QComboBox {{'
                   f'color: {BLACK_COLOR};'
                   f'}}')

LABEL_STYLE = (f''
               f'color: {WIDGET_BG_COLOR};')

BIG_FONT = QFont()
BIG_FONT.setFamily('Ubuntu')
BIG_FONT.setBold(True)
BIG_FONT.setPointSize(15)
