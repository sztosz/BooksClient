from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton


class BooksDetailDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Books Details')

        self.book_name_label = QLabel('Book Name:')
        self.book_name_input = QLineEdit()
        self.book_name_layout = QHBoxLayout()
        self.book_name_layout.addWidget(self.book_name_label)
        self.book_name_layout.addWidget(self.book_name_input)

        self.book_isbn_label = QLabel('Book ISBN:')
        self.book_isbn_input = QLineEdit()
        self.book_isbn_layout = QHBoxLayout()
        self.book_isbn_layout.addWidget(self.book_isbn_label)
        self.book_isbn_layout.addWidget(self.book_isbn_input)

        self.accept_button = QPushButton()
        self.cancel_button = QPushButton()
        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.accept_button)
        self.button_layout.addWidget(self.cancel_button)

        self.layout = QVBoxLayout(self)
        self.layout.addLayout(self.book_name_layout)
        self.layout.addLayout(self.book_isbn_layout)
        self.layout.addLayout(self.button_layout)
        self.setLayout(self.layout)

