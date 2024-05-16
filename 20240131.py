def emailgen(fname: str, lname: str, orgdomain: str):
    emailstr = f"{fname.lower()[0]}.{lname.lower()[0:4]}@{orgdomain}"
    return emailstr


print(
    emailgen(
        input("First name: "),
        input("Last name:"),
        input("Organization domain: ")
    )
)
