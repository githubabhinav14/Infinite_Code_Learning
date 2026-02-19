#using slicing
arr = [1,2,3,4,5]
print(arr[::-1])

#using rverse()
arr = [1,2,3,4,5]
arr.reverse()
print(arr)

#using loop
arr = [10,20,30,40,50]
reversed_arr = []

for i in range(len(arr)-1,-1,-1):
    reversed_arr.append(arr[i])
print(reversed_arr)


