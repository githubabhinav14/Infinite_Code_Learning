#genral input
n = int(input())



# multiple lines in input
n =int(input("Enter range:"))
arr =[]

for i in range(n):
    value = int(input())
    arr.append(value)
print(arr)


#sequnece input
arr = list(map(int, input("Enter numbers separated by space: ").split()))
print("Array is:", arr)

