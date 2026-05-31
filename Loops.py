n = int(input())

for i in range(1, 11):
    print(n, "*", i, "=", n*i)

    n = int(input())
s = 0

for i in range(1, n+1):
    s += i

print(s)

