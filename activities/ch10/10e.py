myArray: list = []
# Population
for row_ptr in range(2):
    row = []
    for col_ptr in range(9):
        row.append(input(f"Value at pos ({row_ptr}, {col_ptr}): "))
    myArray.append(row)
print(myArray)
output = ""
for row in myArray:
    output += " ".join(row) + "\n"
print(output)
