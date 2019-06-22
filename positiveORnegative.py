# A program to check if the number is positive or negative

# PRE-REQUISITES
# 0 is neither positive or negative

# Let's tart with creating the find number is +ve or -ve or 0

def posORneg(num):
    if (num == "q"):
        return "Invalid or not Real"
    elif (num > 0):
        return "Positive"
    elif (num < 0):
        return "Negative"
    elif (num == 0):
        return "Zero"
    else:
        return "Invalid or not Real"


while True:
    try:
        user_input = float(input("Enter the number which you wish to check is +ve or -ve"))
    except ValueError:
        print("Invalid Input!!")
        user_input = "q"
    finally:
        print("The number is ", posORneg(user_input))
