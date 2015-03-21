import operator
from PyQt5.QtCore import QAbstractTableModel, Qt, QModelIndex
from services.DataProxy import DataProxy


class BooksModel(QAbstractTableModel):

    data_proxy = DataProxy()
    headers = []

    def __init__(self, parent, *args):
        super().__init__(parent, *args)
        self.__data = self.data_proxy.get_all_books()
        self.get_headers()

    def get_headers(self):
        for key in self.__data[0]:
            self.headers.append(key)

    def rowCount(self, parent):
        return len(self.__data)

    def columnCount(self, parent):
        return len(self.headers)

    def data(self, index, role=None):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.__data[index.row()][self.headers[index.column()]]

    def headerData(self, column, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.headers[column]
        return None

    def sort(self, column, order):
        self.layoutAboutToBeChanged.emit()
        self.__data = sorted(self.__data,
                           key=operator.itemgetter(self.headers[column]))
        if order == Qt.DescendingOrder:
            self.__data.reverse()
        self.layoutChanged.emit()

    def insertRows(self, row=0, index_parent=None, data=None, *args, **kwargs):
        self.beginInsertRows(QModelIndex(), 0, 0)
        if data:
            self.__data.append(data)
        self.endInsertRows()

    def setData(self, index, data, role=Qt.EditRole):
        if not index.isValid() or role != Qt.EditRole:
            return False
        self.__data[index.row()] = data
        self.dataChanged.emit(index, index)
        return True

    def get_data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        if index.row() > len(self.__data):
            return None

        if role == Qt.DisplayRole or role == Qt.EditRole:
            return self.__data[index.row()]

        return None



