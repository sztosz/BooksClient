from PyQt5.QtWidgets import QPushButton
from views import PersonsDialog
from widgets import SortableQTableView
from models import PersonsModel


class ShowRentingPersonsController():
    def __init__(self):
        self.persons_dialog = PersonsDialog()

        self.persons_view = SortableQTableView(self.persons_dialog)
        self.persons_model = PersonsModel(self.persons_view)
        self.persons_view.setModel(self.persons_model)
        self.persons_dialog.layout.addWidget(self.persons_view)

        self.persons_dialog.add_person_button = QPushButton('Add Person')
        self.persons_dialog.layout.addWidget(self.persons_dialog.add_person_button)

        self.persons_dialog.add_person_button.clicked.connect(self.on_add_person)

        self.persons_dialog.show()

    def on_add_person(self):
        self.add_person_controller = None