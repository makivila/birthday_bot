class IncorrectFormatException(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return f'Incorrect format: {self.message}. Example: Ivanov Ivan - 2000/06/24'
