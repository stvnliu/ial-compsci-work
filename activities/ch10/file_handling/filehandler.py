with open("test.txt", "r+") as file:
    cont = True
    while cont:
        line = input("> ")
        if line == "":
            file.close()
            break
        else:
            file.write(line+"\n")
file = open("test.txt", "r")
print(file.read())
file.close()
