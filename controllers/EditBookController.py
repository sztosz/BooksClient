from controllers import BookController


class EditBookController(BookController):

    def __init__(self, parent, index, book):
        super().__init__(parent)
        self.index = index
        self.book = book

        self.books_detail_dialog.accept_button.setText('Edit Book')

        self.books_detail_dialog.book_name_input.setText(self.book['name'])
        self.books_detail_dialog.book_isbn_input.setText(self.book['isbn'])

        self.books_detail_dialog.show()


    def on_accept(self):
        if self.books_detail_dialog.book_name_input.text() and self.books_detail_dialog.book_name_input.text():
            book = self.set_book_details()
            self.parent.books_model.setData(self.index, data=self.data_proxy.edit_book(self.book['id'], book))
        self.books_detail_dialog.close()
