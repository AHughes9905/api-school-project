import requests

class Quotes:
    def __init__(self):
        self.api_url = "https://ron-swanson-quotes.herokuapp.com/v2/quotes"



    def getData(self):
        """
        Retrieves a random Ron Swanson quote.
        args: self
        return: a completion code and and a Ron Swanson quote as a string
        """
        r = requests.get(self.api_url)
        self.r = r

    def response(self):
        """
        prints raw data retrieved from API
        args: self
        return: prints raw data from API
        """
        print(self.r)
