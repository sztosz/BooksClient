from PyQt5.QtWidgets import QPushButton
from views import BooksDialog
from controllers import AddBookController
from widgets import SortableQTableView
from models import BooksModel

class ShowBooksController():
    def __init__(self):
        self.books_dialog = BooksDialog()

        self.books_view = SortableQTableView(self.books_dialog)
        self.books_model = BooksModel(self.books_view)
        self.books_view.setModel(self.books_model)
        self.books_dialog.layout.addWidget(self.books_view)

        self.books_dialog.add_book_button = QPushButton('Add Book')
        self.books_dialog.layout.addWidget(self.books_dialog.add_book_button)

        self.books_dialog.add_book_button.clicked.connect(self.on_add_book)

        self.books_dialog.show()

    def on_add_book(self):
        self.add_book_controller = AddBookController(self)
