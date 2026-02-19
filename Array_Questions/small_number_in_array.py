n = int(input("Enter n range:"))
arr = []

for i in range(n):
    value = int(input())
    arr.append(value)

smallest = arr[0]

for i in arr:
    if i<smallest:
        smallest = i
print(smallest)