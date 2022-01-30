def is_leap(year):
    leap = True
    notleap = False
    if year%4==0 and year%100==0 and year%400==0:
        return leap
    elif year%4==0 and year%100==0 and year%400!=0:
        return notleap
    elif year%4==0 and year%100!=0 and year%400==0:
        return notleap
    elif year%4==0 and year%100!=0 and year%400!=0:
        return leap
    else:
        return notleap
