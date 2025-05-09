# Homework: Write a class that will take in the month, day, year and will be the date. 
# Write a method that will determine if the year is a leap year. 
# Write a method that will advance the date by one day. 
# Write a method that will move the date the the day before. 
# Write a method that will move the date by a given input. 

class date:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def is_leap_year(self):
        if self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 != 0):
            return True

    def days_in_month(self, month, year):
        if month is None:
            month = self.month
        if year is None:
            year = self.year
        if month == 2:
            if self.is_leap_year():
                return 29
            else:
                return 28
        elif month in [4, 6, 9, 11]:
            return 30
        else:
            return 31

    def advance_day(self):
        self.day += 1
        if self.day > self.days_in_month():
            self.day = 1
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.day += 1
    
    def previous_day(self):
        self.day -= 1
        if self.day < 1:
            self.month -= 1
            if self.month  < 1:
                self.month = 12
                self.year -= 1
            self.day = self.days_in_month(self.month, self.year)
    
    def move_date(self, days):
        if days > 0:
            for i in range(days):
                self.advance_day()
        elif days < 0:
            for i in range(-days):
                self.previous_day()
    
    def __str__(self):
        return month_str + "/" + day_str + "/" + year_str