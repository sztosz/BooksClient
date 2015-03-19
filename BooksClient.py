from PyQt5.QtWidgets import QDialog, QVBoxLayout, QApplication
from PyQt5.QtCore import QCoreApplication
from widgets.BooksQTableView import BooksQTableView


class BooksClient(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Books Rental')

        books_view = BooksQTableView(self)

        layout = QVBoxLayout(self)
        layout.addWidget(books_view)
        self.setLayout(layout)


if __name__ == '__main__':

    # Needed fo my VirtualEnv
    QCoreApplication.setLibraryPaths(['../BooksClientVenv/Lib/site-packages/PyQt5/plugins'])


    app = QApplication([])
    win = BooksClient()
    win.show()
    app.exec_()
