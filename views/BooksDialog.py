from PyQt5.QtWidgets import QDialog, QVBoxLayout

class BooksDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Books')

        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)


