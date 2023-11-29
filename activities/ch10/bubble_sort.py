# import random                                 # For testing sequence
def generate_test_seq(length: int):
    arr = []
    for i in range(length):
        arr.append(random.randint(0, 100))
    return arr
arr = [i for i in range(20)]
print(arr)
sortcount = 0
index = 0
diff = 0
numiter = 0
while True:
    if sortcount == len(arr) - diff - 1:        # Magic number, don't know why it works but it works
        break
    index = 0
    sortcount = 0
    while index < len(arr) - diff - 1:
        if arr[index] < arr[index+1]:           # Not in order, sorting is needed
            swp = arr[index]
            arr[index] = arr[index+1]
            arr[index+1] = swp
        else:
            sortcount += 1
        index += 1
        numiter += 1
        # print(arr)                            # for debug
    diff += 1                                   # At the end of each iteration, we know that the last element in the array is sorted. It is unnecessary to check up to that location in the next iteration.

# Output result
print(arr)
print(f"Done in {numiter} iterations.")
