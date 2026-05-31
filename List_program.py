#Largest element
arr = [10, 50, 20, 90, 30]

print(max(arr))
#second largest
arr = [10, 50, 20, 90, 30]

arr.sort()
print(arr[-2])
#remove duplication
arr = [1,2,2,3,4,4]

print(list(set(arr)))