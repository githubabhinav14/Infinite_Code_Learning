arr = list(map(int, input("Enter a array: ").split()))

rev= []
for i in range(len(arr)-1,-1,-1):
    rev.append(arr[i])
print(rev)

