def q1():
    width = float(input("width: "))
    length = float(input("length: "))
    print(f"The surface area is {width * length}")
def q2():
    degFah = float(input("Temperature in Fahrenheit: "))
    degCel = (degFah - 32) * 5 / 9
    print(f"The converted temperature in degrees celsius is {round(degCel, 1)}") 
def q3():
    tempDegCel = float(input("Temperature in degrees Celsius: "))
    if tempDegCel > 0: print("Temperature is not freezing")
    else: print("Temperature is freezing")
def q4():
    TempDegCel = float(input("Temperature of water in degrees Celsius: "))
    if TempDegCel < 0: print("Water is frozen")
    elif TempDegCel >= 100: print("Water is boiling")
    else: 
        print("Water is liquid")
    return
def q5():
    months = [
        "January", "February", "March", "April", "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]
    index = int(input("Index of month: "))
    if index > 12 or index < 1: print("Invalid")
    print(months[index - 1])
    return
def q6():
    num = int(input("Input positive integer: "))
    while num <= 0:
        num = int(input("Please re-enter the POSITIVE INTEGER: "))
    output = ""
    for i in range(num):
        output += str(i+1) + " "
    print(output)
    return
def q7():
    num_end = int(input("Input positive integer as ending: "))
    while num_end <= 0:
        num_end = int(input("Please re-enter the POSITIVE INTEGER: "))
    stack = []
    output = ""
    for num in range(num_end):
        stack.append(num)
    for _ in range(len(stack)):
        output += str(stack.pop()+1) + " "
    print(output)
# q1()
# q2()
# q3()
# q4()
# q5()
q6()
q7()