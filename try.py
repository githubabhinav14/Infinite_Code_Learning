n =int(input("Enter N:"))
arr = list(map(int, input("Enter Array Values: ").split()))

excepted = n*(n+1)//2
actual = sum(arr)

print("missing number is:", excepted - actual)

