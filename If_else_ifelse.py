#Even&odd
n = int(input())
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

#Largest of 3 Numbers
a, b, c = map(int, input().split())

if a >= b and a >= c:
    print(a)
elif b >= c:
    print(b)
else:
    print(c)