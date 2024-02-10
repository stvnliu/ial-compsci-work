statement = input("Calculator operation(+, -, *, /): ")
match statement:
    case "+":
        rtotal = 0
        while True:
            inp = input("a number (X) to terminate: ")
            if inp == 'X':
                break
            rtotal += float(inp)
        print(f"Sum of calculation is {rtotal}")
    case "-":
        rtotal = 0
        while True:
            inp = input("a number (x) to terminate: ")
            if inp == 'X':
                break
            rtotal -= float(inp)
        print("Calculation result is ", rtotal)
    case "*":
        rtotal = 0
        while True:
            inp = input("a number (x) to terminate: ")
            if inp == 'X':
                break
            rtotal *= float(inp)
            print("Calculation result is ", rtotal)
    case "/":
        rtotal = 0
        while True:
            inp = input("a number (x) to terminate: ")
            if inp == 'X':
                break
            if inp == 0:
                print("Dividing by zero! Err, exiting...")
                break
            rtotal /= float(inp)
        print("Calculation result is ", rtotal)
    case _:
        print("Invalid operation")
