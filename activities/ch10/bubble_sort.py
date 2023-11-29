import random                                   # For testing sequence
def generate_test_seq(length: int):
    arr = []
    for i in range(length):
        arr.append(random.randint(0, 100))
    return arr
TESTING_ITERATIONS = 10
def bubble_sort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                swapped = True
                swp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = swp
        if not swapped:
            return
def verify(arr):
    for index in range(len(arr)-1):
        if arr[index] > arr[index+1]: return False
    return True
# Output result
if __name__ == "__main__":
    for i in range(TESTING_ITERATIONS):
        arr = generate_test_seq(10)
        bubble_sort(arr)
        print(arr)
    print(f"Testing for {TESTING_ITERATIONS} arrays completed.")