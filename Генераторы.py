def allvariants(n):
    for length in range(1, len(n) + 1):
        for start in range(len(n) - length + 1):
            yield n[start:start + length]
all = "abc"
for i in allvariants(all):
    print(i)