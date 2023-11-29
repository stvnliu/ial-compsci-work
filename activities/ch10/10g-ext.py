import random
def generate_random(length: int):
    arr = []
    for i in range(length):
        arr.append(random.randint(0, 100))
    return arr
def generate_seq(length: int):
    arr = []
    for i in range(length): arr.append(i)
    return arr
testarr = generate_seq(30)
testarr[20] = 5
testarr[21] = 5
testpos = []
testfor = int(input("Number: "))
index = 0
count = 0
while index < len(testarr):
    if testarr[index] == testfor:
        testpos.append(str(index))
        count+=1
    index+=1
print(f"{testfor} found {count} times at positions {' '.join(testpos)}.") if count > 0 else print("Item not found.")
