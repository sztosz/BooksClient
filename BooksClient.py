from PyQt5.QtWidgets import QDialog, QVBoxLayout, QApplication
from PyQt5.QtCore import QCoreApplication
from controllers import ShowBooksController


if __name__ == '__main__':

    # Needed fo my VirtualEnv
    # QCoreApplication.setLibraryPaths(['../BooksClientVenv/Lib/site-packages/PyQt5/plugins'])


    app = QApplication([])
    win = ShowBooksController()
    app.exec_()
