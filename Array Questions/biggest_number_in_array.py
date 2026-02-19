n = int(input())
arr = []

for i in range(n):
    value = int(input())
    arr.append(value)

biggest = arr[0]

for num in arr:
    if num>biggest:
        biggest = num
print(biggest)