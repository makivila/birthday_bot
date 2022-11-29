from utils import convert_to_date
from errors import IncorrectFormatException
from enums import BirthdayType


class BirthdayData():
  def __init__(self, user_id , name, birthday_type):
    self.user_id = user_id 
    self.birthday_type = birthday_type
    if birthday_type == BirthdayType.today:
        self.name_str = "Today’s birthday: " + name
    else: 
        self.name_str = "Tomorrow’s birthday: " + name
    
class Service():
    def __init__(self, repository):
        self.repository = repository

    def add_birthday_date(self, text, user_id):  
        name_date = text.split(" - ")
        if len(name_date) != 2:
           raise IncorrectFormatException("invalid string")  
        name = name_date[0]
        try: 
            date = convert_to_date(name_date[1])
        except:
            raise IncorrectFormatException("invalid date entered")
        self.repository.add_birthday_date(date, name, user_id)
        
    def get_birthdays(self):
        today_birthdays = self.repository.get_today_birthdays()
        tomorrow_birthdays = self.repository.get_tomorrow_birthdays()
        birthday_datas = []
        for data in today_birthdays:
            birthday_datas.append(BirthdayData(data[0], data[1], BirthdayType.today))
        for data in tomorrow_birthdays:
            birthday_datas.append(BirthdayData(data[0], data[1], BirthdayType.tomorrow))
        return birthday_datas

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
    
    def get_greeting_by_user_exists(self, user_id):
        result = self.repository.check_user_id(user_id)
        if result:
            answer = 'Bot is working'
        else:
            answer ='''Please, add date and name your friend which birthday you want to remember.
Example: Ivanov Ivan - 24.06.2000'''
        return answer

    def get_all_user_ids(self):
        result = self.repository.get_all_user_ids()
        all_user_ids = []
        for user_id_dict in result:
            all_user_ids.append(user_id_dict[0])
        return all_user_ids



        
        



