high = -1
low = 101
acc = 0
c = 0
marr = []
for i in range(5):
    minp = int(input(f"Mark {i+1}: "))
    while minp < 0 or minp > 100:
        minp = int(input("Mark invalid, retry: "))
    if high == -1 or minp > high:
        high = minp
    if low == 101 or minp < low:
        low = minp
    acc += minp
    c += 1
print("Lowest:", low)
print("Highest:", high)
print("Average:", acc / c)
def stars(string: str):
    print("*"*len(string))
