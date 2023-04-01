from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class TableWidget(QTableWidget):
    def __init__(self, headers, parent=None):
        if parent:
            super().__init__(parent)
        else:
            super().__init__()

        self.setEditTriggers(QTableWidget.NoEditTriggers)

        self.setColumnCount(len(headers))
        self.setRowCount(0)

        self.setHorizontalHeaderLabels(headers)
        self.resizeColumnsToContents()

    def table(self):
        for i in range(self.rowCount()):
            for j in range(self.columnCount()):
                self.set_cell(i, j, '')

    def add_row(self, row):
        self.setRowCount(self.rowCount() + 1)
        if len(row) == self.columnCount():
            for j in range(len(row)):
                self.set_cell(self.rowCount() - 1, len(row) - j - 1, row[j])
        self.resizeColumnsToContents()

    def set_cell(self, i, j, content):
        self.setItem(i, j, TableWidget.cell(TableWidget.format_content(content)))

    def clear(self):
        self.setRowCount(0)

    @staticmethod
    def format_content(content):
        if isinstance(content, int):
            return str(content).strip()
        if isinstance(content, float):
            return f'{content:6g}'.strip()
        if isinstance(content, str):
            return content.strip()
        if isinstance(content, (tuple, list)):
            return '[' + ', '.join([TableWidget.format_content(el) for el in content]) + ']'

    @staticmethod
    def cell(text=''):
        item = QTableWidgetItem()
        item.setText(text)
        return item
