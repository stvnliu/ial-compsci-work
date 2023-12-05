path = input("path of text file you would like to use for read and write: ")
file = open(path, "w+")
while True:
    txt = input("> ")
    if txt == "": break
    file.write(txt)
file.close()
rfile = open(path, "r")
print(rfile.read())
rfile.close()
