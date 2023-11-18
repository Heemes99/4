from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QRectF
import sys
import sqlite3
from PyQt5 import uic

from file_ui import Ui_MainWindow


class Notebook(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect('coffee.sqlite')
        self.cur = self.con.cursor()

        self.pushButton.clicked.connect(self.a)

    def a(self):
        if self.comboBox.currentText() == 'Все':
            res = self.cur.execute('''SELECT *
            FROM coffee''')
        else:
            res = self.cur.execute(f'''SELECT *
            FROM coffee
            WHERE variety = "{self.comboBox.currentText()}"''')
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)

        # Filling the table with elements
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row[1:]):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Notebook()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())