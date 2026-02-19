n = int(input())
arr = []
for i in range(n):
    value = int(input())
    arr.append(value)

smallest = arr[0]

for num in arr:
    if num<smallest:
        smallest = num
print(smallest)