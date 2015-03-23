from PyQt5.QtCore import Qt, QSortFilterProxyModel, QRegExp
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QPushButton, QMenu, QLineEdit, QComboBox
from views import BooksDialog
from controllers import AddBookController, EditBookController
from widgets import BooksQTableView
from models import DataModel


class ShowBooksController():
    def __init__(self):
        self.books_dialog = BooksDialog()

        self.books_view = BooksQTableView(self.books_dialog)
        self.books_model = DataModel(self.books_view)

        self.proxy = QSortFilterProxyModel(self.books_model)
        self.proxy.setSourceModel(self.books_model)

        self.books_view.setModel(self.proxy)

        self.books_dialog.search_input = QLineEdit()
        self.books_dialog.search_combo_box = QComboBox()
        self.books_dialog.search_combo_box.addItems(self.books_model.headers)

        self.books_dialog.layout.addWidget(self.books_dialog.search_input)
        self.books_dialog.layout.addWidget(self.books_dialog.search_combo_box)

        self.books_dialog.layout.addWidget(self.books_view)

        self.books_dialog.add_book_button = QPushButton('Add Book')
        self.books_dialog.layout.addWidget(self.books_dialog.add_book_button)

        self.books_view.setContextMenuPolicy(Qt.CustomContextMenu)

        self.books_dialog.add_book_button.clicked.connect(self.on_add_book)
        self.books_view.customContextMenuRequested.connect(self.show_context_menu)
        self.books_dialog.search_input.textChanged.connect(self.on_search)
        self.books_dialog.search_combo_box.currentIndexChanged.connect(self.on_change_search_column)

        self.books_dialog.show()

    def show_context_menu(self, event):
        index = self.books_view.indexAt(event)

        menu = QMenu(self.books_view)
        menu.addAction('Edit Book', lambda: self.on_edit_book(index))
        menu.addAction('Remove Book')
        menu.exec_(QCursor.pos())

    def on_add_book(self):
        self.add_book_controller = AddBookController(self)

    def on_edit_book(self, index):
        self.edit_book_controller = EditBookController(self, index, self.books_model.get_data(index))

    def on_search(self, text):
        search = QRegExp(text, Qt.CaseInsensitive, QRegExp.RegExp)
        self.proxy.setFilterRegExp(search)

    def on_change_search_column(self, index):
        self.proxy.setFilterKeyColumn(index)
