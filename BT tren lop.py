

class Restaurant():
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(self.name)
        print(self.type)
    def open_restaurant(self):
        print("open")

