from datetime import datetime


def convert_to_date(date): 
    return datetime.strptime(date, '%d.%m.%Y')