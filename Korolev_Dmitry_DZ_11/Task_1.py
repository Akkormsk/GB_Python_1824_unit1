from datetime import datetime


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def str_to_type(cls, str_date):
        day, month, year = map(int, str_date.split('-'))
        date_cls = cls(day, month, year)
        return date_cls

    @staticmethod
    def valid_date(str_date):
        day, month, year = map(int, str_date.split('-'))
        return True if day <= 31 and month <= 12 and year <= datetime.now().year else False


my_date = Date.str_to_type('22-10-2222')
print(my_date.month)
print(Date.valid_date('22-10-2002'))
