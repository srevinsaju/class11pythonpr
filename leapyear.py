# this is the program to check if the given year is a leap year or not

def leapyr(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
               return True
            else:
                return False
        else:
            return True
    else:
        return False

running = True
while running:
    try:
        usr_year = int(input("Enter the year "))
    except ValueError:
        print("Error. Invalid Input. Quitting")
        break
    if leapyr(usr_year):
        print("The year is a leap year")
    else:
        print("The year is not a leap year")
