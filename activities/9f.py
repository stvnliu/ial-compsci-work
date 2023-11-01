password = input("input password: ")
password_verify = input("verify your password: ")
if password_verify != password:
    print("Password verification insuccessful")
    exit()
tries = 0
password_input = None
successful = False
while tries < 3 and not successful:
    password_input = input(f"Input your password, you have {3 - tries} attempts left: ")
    if password_input == password:
        print("password correct!")
        successful = True
    else:
        print("password incorrect!")
    tries += 1
print("Logged in!" if successful else "Maximum amount of tries exceeded!")
