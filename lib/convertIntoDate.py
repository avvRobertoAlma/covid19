from datetime import datetime

def convertIntoDate(str_date):
    date_obj = datetime.strptime(str_date.split()[0], '%Y-%m-%d')
    return date_obj
