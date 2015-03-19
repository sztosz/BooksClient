import requests


class ApiClient():
    def __init__(self, url):
        self.url = url
        pass

    def get_all_books(self):
        response = requests.get(self.url + '/books/')
        return response.json()

    def get_book(self, id):

        pass

    def get_all_renting_persons(self):
        pass

    def get_renting_person(self, id):
        pass

    def get_all_rented_books(self):
        response = requests.get(self.url + '/books-rented/')
        return response.json()

    def get_rented_book(self, id):
        pass


