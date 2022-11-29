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
    def get_today_birthdays(self, cursor):
        query = """SELECT user_id, name,
                   (YEAR(CURRENT_DATE) - YEAR(date)) AS age
                   FROM birthday_friends WHERE DAY(date) = DAY(CURDATE()) 
                   AND MONTH(date) = MONTH(CURDATE())"""      
        cursor.execute(query)
        return cursor.fetchall() 

    @cursor_handler
    def get_tomorrow_birthdays(self, cursor):
        query = """SELECT user_id, name, 
                    (YEAR(CURRENT_DATE) - YEAR(date)) AS age
                    FROM birthday_friends 
                    WHERE DAY(date) = DAY(CURDATE() + 1) 
                    AND MONTH(date) = MONTH(CURDATE())"""      
        cursor.execute(query)
        return cursor.fetchall() 
        
    @cursor_handler
    def get_all_birthdays(self, cursor, user_id):
        query = """SELECT name, date 
                            FROM birthday_friends 
                            WHERE user_id = %s"""
        query_args = (user_id, )                    
        cursor.execute(query, query_args)
        return cursor.fetchall() 
    
    @cursor_handler
    def check_user_id(self, cursor, user_id):
        query = """SELECT user_id 
                            FROM birthday_friends 
                            WHERE user_id = %s
                            LIMIT 1"""
        query_args = (user_id, )                    
        cursor.execute(query, query_args)
        return cursor.fetchall() 

    @cursor_handler
    def get_all_user_ids(self, cursor):
        query = 'SELECT DISTINCT user_id FROM birthday_friends'
        cursor.execute(query)
        return cursor.fetchall()

