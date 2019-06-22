# program to find who is the elder one among the others
a = []
theEldest = [0]
tmptheEldest = [None]
running = True
while running == True:
    try:
        a.append(float(input("Input the age of the person. Press 0 to stop ")))
    except ValueError:
        print("Invalid Output")
        continue
    if (a[-1] == 0):
        running = False

for i in a:
    if (theEldest[0] == None):
        theEldest = i
    elif i > theEldest[0]:
        theEldest[0] = i
    elif i == theEldest[0]:
        theEldest = i
    else:
        pass

print("The eldest person is ", theEldest)
