def dayOfProgrammer(year):
    day_to_find = 256
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if year <= 1917 and year % 4 == 0:
        days_in_months[1] = 29
    elif year == 1918:
        days_in_months[1] = 15 # 28 - 13
    elif year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        days_in_months[1] = 29
        
    mm = 0
    total_days = 0
    
    while (total_days + days_in_months[mm]) <= day_to_find:
        total_days += days_in_months[mm]
        mm += 1
        
    dd = day_to_find - total_days
    mm += 1
    
    day_of_the_programmer = f"{dd:02d}.{mm:02d}.{year}"
    
    return day_of_the_programmer
