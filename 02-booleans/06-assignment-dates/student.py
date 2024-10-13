# write your code here
def is_valid_month(month):
    return month >= 1 and month <= 12
print(is_valid_month(13))

def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

print(is_leap_year(400))

def has_30_days(month):
    return month == 4 or month == 6 or month == 9 or month == 11
print(has_30_days(4))

def has_28_days(month, year):
    return month == 2 and year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(has_28_days(2, 9))

def has_29_days(month, year):
    return month == 2 and year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(has_29_days(2,4))

def has_30_days(month):
    return month in (4, 6, 9, 11)

def is_valid_date(day, month, year):
    return (
        (1 <= month <= 12) and  
        (
            (has_30_days(month) and 1 <= day <= 30) or 
            (month == 2 and 1 <= day <= 29 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))) or 
            (month == 2 and 1 <= day <= 28) or  
            (1 <= day <= 31)  
        )
    )

