class FullException(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return "Error : " + self.message + " is full"