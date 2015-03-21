import requests


class ApiClient():
    def __init__(self, url):
        self.url = url
        pass

    def get_all_books(self):
        response = requests.get(self.url + '/books/')
        return response.json()

    def get_book(self, _id):
        pass

    def edit_book(self, _id, book):
        response = requests.put(self.url + '/books/' + str(_id) + '/', book)
        return response.json()

    def put_book(self, book):
        response = requests.post(self.url + '/books/', book)
        return response.json()

    def get_all_renting_persons(self):
        pass

    def get_renting_person(self, _id):
        pass

    def get_all_rented_books(self):
        response = requests.get(self.url + '/books-rented/')
        return response.json()

    def get_rented_book(self, _id):
        pass


