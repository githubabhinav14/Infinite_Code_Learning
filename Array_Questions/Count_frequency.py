arr = list(map(int, input("Enter values:").split()))

freq = {}

for num in arr:
    if num in freq:
        freq += 1
    else:
        freq = 1
for key in freq:
    print(key, freq[key])