n =input()
res = ""
for i in n:
    if i.lower() in "aeiou":
        res += "*"
    else:
        res += i
print(res)