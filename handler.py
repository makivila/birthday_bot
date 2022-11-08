import time

class Handler:
    def __init__(self, bot, servises):
        self.bot = bot  
        self.servises = servises
    def run(self):
        @self.bot.message_handler(commands=["start"])
        def start(message, res=False):
            self.notification(message)
        @self.bot.message_handler(content_types=["text"])
        def text(message):
            self.init_text_handler(message)
        self.bot.polling(none_stop=True, interval=0)

    def init_text_handler(self, message):
        if message.text == 'All birthday':
            self.all_birthdays(message)
        else:
            self.add_birthday_date(message)


    def add_birthday_date(self, message): 
        try:
            self.servises.add_birthday_date(message.text, message.chat.id)
            answer = 'Note has added successfully'
        except Exception as e:
            answer = e      
        self.bot.send_message(message.chat.id, answer)
    
    def all_birthdays(self, message):
        try:
            answer = self.servises.get_all_birthdays(message.chat.id)
        except Exception as e:
            answer = e      
        self.bot.send_message(message.chat.id, answer)

    def notification(self, message):
        while True:
            try:
                answer = self.servises.get_today_birthdays(message.chat.id)
            except Exception as e:
                answer = e
            if answer != None:
                self.bot.send_message(message.chat.id, answer)
            time.sleep(42000)


