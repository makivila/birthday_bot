import time

  
def is_date(date):
    try:
        time.strptime(date, '%Y/%m/%d')
        return True
    except ValueError:
        return False 


    