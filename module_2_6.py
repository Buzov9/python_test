n = int(input("число на первой вставке: "))
# n = 6

result = []
if n % 2 == 0:
    n2 = n/2
    n2 = int(n2)
    for i1 in range(1, n2 + 1):
        for j1 in range(i1 + 1, n2 + 1):
            if (i1 + j1) == n2:
                result.append((i1, j1))

for i in range(1, n+1):
    for j in range(i+1, n+1):
        if (i + j) == n:
            result.append((i, j))
print(*result)

