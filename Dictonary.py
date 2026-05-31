student = {
    "name":"Bhoomi",
    "age":20
}

print(student["name"])

#frequency count
s = "python"

d = {}

for ch in s:
    d[ch] = d.get(ch,0)+1

print(d)