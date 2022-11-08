from utils import is_date
from errors import IncorrectFormatException

class Service():
    def __init__(self, repository):
        self.repository = repository

    def add_birthday_date(self, text, user_id):  
        name_date = text.split(" - ")
        if len(name_date) != 2:
           raise IncorrectFormatException("invalid string")  
        name = name_date[0]
        date = name_date[1]

        if not is_date(date): 
            raise IncorrectFormatException("invalid date entered")
        self.repository.add_birthday_date(date, name, user_id)

    def get_today_birthdays(self, user_id):
        result = self.repository.get_today_birthdays(user_id)
        if not result:
            return None
        answer = 'Today birthday: '
        for name in result:
            answer += name[0] + ' '
        return answer

    def get_all_birthdays(self, user_id):
        result = self.repository.get_all_birthdays(user_id)
        if not result:
            return 'There is no birthdays in DB'
        answer = 'Birthdays: '
        for i in range(len(result)):
            if i == len(result)-1:
                sep = ' .'
            else:
                sep = ' , '
            answer += result[i][0] + ' - ' + str(result[i][1]) + sep         
        return answer

        
        



