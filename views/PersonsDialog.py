from PyQt5.QtWidgets import QDialog, QVBoxLayout


class PersonsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Persons')

        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)