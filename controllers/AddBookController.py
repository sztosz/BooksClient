from views import BooksDetailDialog


class AddBookController():

    def __init__(self):
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
        print('accept clicked')
        self.books_detail_dialog.close()
