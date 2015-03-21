from controllers import BookController


class AddBookController(BookController):

    def __init__(self, parent):
        super().__init__(parent)
        self.books_detail_dialog.accept_button.setText('Add Book')

        self.books_detail_dialog.show()

    def on_accept(self):
        if self.books_detail_dialog.book_name_input.text() and self.books_detail_dialog.book_name_input.text():
            book = self.set_book_details()
            self.parent.books_model.insertRows(data=self.data_proxy.put_book(book))
        self.books_detail_dialog.close()
