def arTriangle(height=0.0, base=0.0, sidea=0.0, sideb=0.0, sidec=0.0):
    if (height == 0 and base == 0):
        s = (sidea + sideb + sidec) / 2
        return (s * (s - sidea) * (s - sideb) * (s - sidec)) ** (1 / 2)
    elif sideb == 0 and sidea == 0 and sidec == 0:
        return 1 / 2 * height * base
    else:
        print("The required information is not met..")


def arsquare(height=0.0, base=0.0):
    return height * base


print("Hello")
print("A program to find the area of the area of a square or the triangle")
running = True
while running:
    triorquad = input("Enter the option (t/s/r)")

    if (triorquad == "s"):
        print("SQUARE")
        side = float(input("Enter side"))
        print("The area is ", arsquare(height=side, base=side))
    elif (triorquad == "q"):
        print("RECTANGLE")
        leng = float(input("Enter the length of retangle"))
        breadth = float(input("Enter the breadth"))
        print("The area is ", arsquare(height=leng, base=breadth))
    elif(triorquad == "")


