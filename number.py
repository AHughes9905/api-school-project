import requests

class Number:
    def __init__(self):
        self.api_url = "http://numbersapi.com/"



    def getData(self, number):
        """
        Retrieves historical event in the year of the inputted number.
        args: the year that the event will be from as a string
        return: a completion code and and a historical event as a string
        """
        self.totapi = self.api_url + number + "/year"
        #self.totapi = "https://api.nytimes.com/svc/topstories/v2/science.json?api-key=" + self.key
        r = requests.get(self.totapi)
        self.r = r

    def response(self):
        """
        prints raw data retrieved from API
        args: self
        return: prints raw data from API
        """
        print(self.r)
