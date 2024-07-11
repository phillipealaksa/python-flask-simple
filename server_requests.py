import requests

class Server:
    def __init__(self):
        self.url = "http://127.0.0.1:5000"
        self.getEnd = "/get-endpoint"
        self.postEnd = "/post-endpoint"

    def status(self):
        try:
            requests.get(self.url)
            return True
        except:
            return False

    def add_house(self, address):
        if not self.status():
            return "Server is down. Cannot add house. Run server.py first"
        data = {
            "address": str(address),
            "action": "addHouse"
        }
        response = requests.post(self.url + self.postEnd, json=data)
        return response.text

    def remove_house(self, address):
        if not self.status():
            return "Server is down. Cannot remove house. Run server.py first"
        data = {
            "address": address,
            "action": "removeHouse"
        }
        response = requests.post(self.url + self.postEnd, json=data)
        return response.text

    def add_person(self, address, person):
        if not self.status():
            return "Server is down. Cannot add person. Run server.py first"
        data = {
            "address": address,
            "person": person.__dict__,
            "action": "addPerson"
        }
        response = requests.post(self.url + self.postEnd, json=data)
        return response.text

    def remove_person(self, address, person):
        if not self.status():
            return "Server is down. Cannot remove person. Run server.py first"
        data = {
            "address": address,
            "person": person.__dict__,
            "action": "removePerson"
        }
        response = requests.post(self.url + self.postEnd, json=data)
        return response.text
    
    def list_people(self, address):
        if not self.status():
            return "Server is down. Cannot remove person. Run server.py first"
        response = requests.get(self.url + self.getEnd, params={"address": address, "list": "False"})
        return response.text

    def get_houses(self):
        if not self.status():
            return "Server is down. Cannot remove person. Run server.py first"
        response = requests.get(self.url + self.getEnd, params={"list": "True"})
        return response.text