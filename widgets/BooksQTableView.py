from PyQt5.QtWidgets import QTableView
from models import BooksModel


class BooksQTableView(QTableView):
    def __init__(self, parent):
        super().__init__(parent)

        self.setModel(BooksModel(parent))
        self.resizeColumnsToContents()
        self.setSortingEnabled(True)
