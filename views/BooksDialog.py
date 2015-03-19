from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton
from widgets import BooksQTableView


class BooksDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Books')

        books_view = BooksQTableView(self)
        self.add_book_button = QPushButton('Add Book')

        layout = QVBoxLayout(self)
        layout.addWidget(books_view)
        layout.addWidget(self.add_book_button)
        self.setLayout(layout)

