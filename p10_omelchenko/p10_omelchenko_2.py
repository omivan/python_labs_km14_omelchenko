from typing import cast
import numpy as np

years = np.arange(1900, 2020+3, 1)

def read_month():
    while(True):
        try:  
            month = int(input("Enter number of month(1 to 12) "))
            if(month > 12 or month <= 0): raise TypeError
            break
        except:
            print("Invalid input, month should be number from 1 to 12")
    return month
def read_year():
    while(True):
        try:  
            year = int(input("Enter number of year(1900 to 2023) "))
            if(year < 1900 or year > 2023): raise TypeError
            break
        except:
            print("Invalid input, year should be number from 1900 to 2023")
    return year

def find_leap_years(years):
    return list(filter(lambda year: (year % 100 != 0 and year % 4 == 0 ) or year % 400 == 0, years))


def days_in_month(find_leap_years, year, month):
    if(month == 1): return 31 #Jan
    if((month == 2) and (year in find_leap_years(years))): return 29 #Feb
    if((month == 2) and (year not in find_leap_years(years))): return 28 # Feb_leap
    if(month == 3): return 31 #Mar
    if(month == 4): return 30 #Apr
    if(month == 5): return 31 #May
    if(month == 6): return 30 #Jun
    if(month == 7): return 31 #Jul
    if(month == 8): return 31 #Aug
    if(month == 9): return 30 #Sep
    if(month == 10): return 31 #Oct
    if(month == 11): return 30 #Nov
    if(month == 12): return 31 #Dec
        
print(find_leap_years(years))
month = read_month()
year = read_year()
print("There are " + str(days_in_month(find_leap_years, year, month)) + " days in " + str(month) + " month of " + str(year))



