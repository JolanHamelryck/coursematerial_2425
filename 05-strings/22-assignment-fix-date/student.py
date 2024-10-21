# write your code here
def fix_date(date):
    # Extract the month, day, and year using slicing
    month = date[0:2]
    day = date[3:5]
    year = date[6:10]
    
    # Return the date in the yyyy/mm/dd format
    return f"{year}/{month}/{day}"
