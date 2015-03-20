from views import BooksDetailDialog
from services import DataProxy


class AddBookController():

    def __init__(self, parent):
        self.parent = parent

        self.data_proxy = DataProxy()
        self.books_detail_dialog = BooksDetailDialog()
        self.books_detail_dialog.accept_button.setText('Add Book')
        self.books_detail_dialog.cancel_button.setText('Cancel')

        self.books_detail_dialog.cancel_button.clicked.connect(self.on_cancel)
        self.books_detail_dialog.accept_button.clicked.connect(self.on_accept)

        self.books_detail_dialog.setModal(True)
        self.books_detail_dialog.show()


    def on_cancel(self):
        self.books_detail_dialog.close()

    def on_accept(self):
        if self.books_detail_dialog.book_name_input.text() and self.books_detail_dialog.book_name_input.text():
            book = {
                'name': self.books_detail_dialog.book_name_input.text(),
                'isbn': self.books_detail_dialog.book_isbn_input.text()
            }
            self.parent.books_model.insertRows(data=self.data_proxy.put_book(book))
        self.books_detail_dialog.close()
