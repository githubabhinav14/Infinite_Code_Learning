def cube(num):
    return num*num*num
sum = 0
for i in range(1,6):
    sum = sum + cube(i)
print(sum)