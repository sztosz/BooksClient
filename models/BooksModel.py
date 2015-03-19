import operator
from PyQt5.QtCore import QAbstractTableModel, Qt
from services.DataProx import DataProxy


class BooksModel(QAbstractTableModel):

    data_proxy = DataProxy()
    headers = []

    def __init__(self, parent, *args):
        super().__init__(parent, *args)
        self.data = self.data_proxy.get_all_books()
        print(self.data)
        self.get_headers()

    def get_headers(self):
        for key in self.data[0]:
            self.headers.append(key)

    def rowCount(self, parent):
        return len(self.data)

    def columnCount(self, parent):
        return len(self.headers)

    def data(self, index, role=None):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.data[index.row()][self.headers[index.column()]]

    def headerData(self, column, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.headers[column]
        return None

    def sort(self, column, order):
        self.layoutAboutToBeChanged.emit()
        self.data = sorted(self.data,
                           key=operator.itemgetter(self.headers[column]))
        if order == Qt.DescendingOrder:
            self.data.reverse()
        self.layoutChanged.emit()


