# A program to check if the number is odd or even

def even_or_odd(num):
    if num == "q":
        return "Invalid"
    elif num % 2 == 0:
        return "Even"
    else:
        return "Odd"


while True:
    try:
        user_input = float(input("Enter then number you would like to check is odd or even"))
    except ValueError or TypeError:
        user_input = "q"
    finally:
        print("The number is ", even_or_odd(user_input))
