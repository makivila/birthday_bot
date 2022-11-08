

class Repository ():
    def __init__(self, db):
        self.db = db
    
    def cursor_handler(func):
        def decorator(self, *args, **kwargs):
            if not self.db.is_connected():
                self.db.reconnect()
            cursor = self.db.cursor()
            result = func(self, cursor, *args, **kwargs)
            cursor.close()
            self.db.commit()
            return result
        return decorator
        
    @cursor_handler
    def add_birthday_date(self, cursor, date, name, user_id):
        query = """INSERT INTO birthday_friends (user_id, date, name) 
                                        VALUES (%s,%s,%s)"""
        query_args = (user_id, date, name)
        cursor.execute(query, query_args)
        
    @cursor_handler
    def get_today_birthdays(self, cursor, user_id):
        query = """SELECT name 
                            FROM birthday_friends 
                            WHERE date = CURDATE()
                            AND user_id = %s"""
        query_args = (user_id, )                    
        cursor.execute(query, query_args)
        return cursor.fetchall() 
        
    @cursor_handler
    def get_all_birthdays(self, cursor, user_id):
        query = """SELECT name, date 
                            FROM birthday_friends 
                            WHERE user_id = %s"""
        query_args = (user_id, )                    
        cursor.execute(query, query_args)
        return cursor.fetchall() 


