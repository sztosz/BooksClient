

class PersonsModel(AbstractModel):
    def __init__(self, parent, *args):
        super().__init__(parent, *args)
        self.data = self.data_proxy.get_all_books()
        self.get_headers()