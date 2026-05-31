#Factorial
n = int(input())

fact = 1
for i in range(1, n+1):
    fact *= i

print(fact)
#Fibonacci series
n = int(input())

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a+b
#prime number
    n = int(input())

flag = True

for i in range(2, int(n**0.5)+1):
    if n % i == 0:
        flag = False
        break

print("Prime" if flag and n > 1 else "Not Prime")
#armstrong number
n = int(input())

temp = n
s = 0

while temp > 0:
    digit = temp % 10
    s += digit ** len(str(n))
    temp //= 10

if s == n:
    print("Armstrong")
else:
    print("Not Armstrong")

