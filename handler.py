import threading
import os
import time
from datetime import datetime
from errors import IncorrectFormatException


class Handler:
    def __init__(self, bot, servises):
        self.bot = bot  
        self.servises = servises
    def run(self):
        @self.bot.message_handler(commands=["start"])
        def start(message, res=False):
            self.greetings(message)
        @self.bot.message_handler(content_types=["text"])
        def text(message):
            self.init_text_handler(message)
        thread = threading.Thread(target=self.notification)
        thread.start()
        while True:
            try:
                self.bot.polling(none_stop=True, interval=0)
            except Exception as e:
                print(e)
                time.sleep(5)

    def init_text_handler(self, message):
        if message.text == 'All birthday':
            self.all_birthdays(message)
        elif message.text.startswith('ADMIN MESSAGE: ') and \
            str(message.chat.id) == os.getenv("ADMIN_USER_ID"):
            self.admin_message(message)
        else:
            self.add_birthday_date(message)

    def add_birthday_date(self, message): 
        try:
            self.servises.add_birthday_date(message.text, message.chat.id)
            answer = 'Note has added successfully'
            self.bot.send_message(message.chat.id, answer)
        except IncorrectFormatException as e:
            self.bot.send_message(message.chat.id, e)
        except Exception as e:      
            self.bot.send_message(os.getenv("ADMIN_USER_ID"), e)
            self.bot.send_message(message.chat.id, 'An error has occurred')
        
    def all_birthdays(self, message):
        try:
            answer = self.servises.get_all_birthdays(message.chat.id)
            self.bot.send_message(message.chat.id, answer)
        except Exception as e:    
            self.bot.send_message(os.getenv("ADMIN_USER_ID"), e)
            self.bot.send_message(message.chat.id, 'An error has occurred')

    def notification(self):
        while True:
            try:
                now = datetime.now() 
                current_time = now.strftime("%H:%M")
                if current_time in ['09:00', '14:00', '20:00']:
                    try:
                        result = self.servises.get_birthdays()
                    except Exception as e:
                        self.bot.send_message(os.getenv("ADMIN_USER_ID"), e)
                    if result:
                        for data in result:
                            try:
                                self.bot.send_message(data.user_id, data.data_str)
                            except Exception as e:
                                print(e)
                time.sleep(60)
            except Exception as e:
                print(e)
                time.sleep(5)
               
    def greetings(self, message):
        try:
            answer = self.servises.get_greeting_by_user_exists(message.chat.id)
            self.bot.send_message(message.chat.id, answer)
        except Exception as e:
            self.bot.send_message(message.chat.id, 'An error has occurred')
            self.bot.send_message(os.getenv("ADMIN_USER_ID"), e)

    def admin_message(self, message):
            result = self.servises.get_all_user_ids()
            message.text = message.text.replace('ADMIN MESSAGE: ', '')
            for user_id in result:
                self.bot.send_message(user_id, message.text)

        

               
      






        

