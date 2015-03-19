from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton
from . import BooksDialog


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.books_dialog = BooksDialog()
        self.setWindowTitle('Books Rental')

        books_button = QPushButton('Books', self)
        books_button.clicked.connect(self.handle_books_button)

        layout = QVBoxLayout(self)
        layout.addWidget(books_button)
        self.setLayout(layout)

        self.show()

    def handle_books_button(self):
        self.books_dialog.setModal(True)
        self.books_dialog.show()
