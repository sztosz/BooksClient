from .ApiClient import ApiClient


class DataProxy():

    url = 'http://books.sztosz.tk/api/v1'
    data_source = ApiClient(url)

    def get_all_books(self):
        return self.data_source.get_all_books()

    def get_book(self, _id):
        pass
    
    def edit_book(self, _id, book):
        return self.data_source.edit_book(_id, book)

    def put_book(self, book):
        return self.data_source.put_book(book)

    def get_all_renting_persons(self):
        pass

    def get_renting_person(self, _id):
        pass

    def get_all_rented_books(self):
        pass

    def get_rented_book(self, _id):
        pass
