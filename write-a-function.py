def is_leap(year):
    leap = False
    
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                leaf = True
        else:
            leaf = True
    
    return leap
