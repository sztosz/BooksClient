from views import BooksDetailDialog
from services import DataProxy


class EditBookController():

    def __init__(self, parent, index, book):
        self.parent = parent
        self.index = index
        self.book = book

        self.data_proxy = DataProxy()
        self.books_detail_dialog = BooksDetailDialog()
        self.books_detail_dialog.accept_button.setText('Edit Book')
        self.books_detail_dialog.cancel_button.setText('Cancel')

        self.books_detail_dialog.book_name_input.setText(self.book['name'])
        self.books_detail_dialog.book_isbn_input.setText(self.book['isbn'])

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
                'isbn': self.books_detail_dialog.book_isbn_input.text(),
                'id': self.book['id'],
            }
            self.parent.books_model.setData(self.index, data=self.data_proxy.edit_book(self.book['id'], book))
        self.books_detail_dialog.close()
