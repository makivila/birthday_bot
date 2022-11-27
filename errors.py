class IncorrectFormatException(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return f'Incorrect format: {self.message}. Example: Ivanov Ivan - 24.06.2000'
