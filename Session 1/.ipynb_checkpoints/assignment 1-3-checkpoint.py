def is_leap_year(year):
    if (year % 4) == 0 and (year % 100) != 0:
        return True
    elif (year % 400) == 0:
        return True
    else:
        return False

year = int(input("Enter year: "))

while year > 0:
    print("Is leap year: " + str(is_leap_year(year)))
    year = int(input("Enter year: "))
