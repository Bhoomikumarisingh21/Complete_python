#Reverse String 
s= input()
print(s[::-1])
#Palindrome
s = input()

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
#Count Vowels
    s = input().lower()

count = 0

for ch in s:
    if ch in "aeiou":
        count += 1

print(count)
