from views import BooksDialog
from controllers import AddBookController


class ShowBooksController():
    def __init__(self):
        self.books_dialog = BooksDialog()
        self.books_dialog.add_book_button.clicked.connect(self.on_add_book)

        self.books_dialog.show()

    def on_add_book(self):
        self.add_book_controller = AddBookController()
