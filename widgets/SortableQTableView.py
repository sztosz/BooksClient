from PyQt5.QtWidgets import QTableView


class SortableQTableView(QTableView):
    def __init__(self, parent):
        super().__init__(parent)

        self.resizeColumnsToContents()
        self.setSortingEnabled(True)
