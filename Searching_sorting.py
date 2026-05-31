#liner search 
arr = [10,20,30,40]
key = 30

for i in range(len(arr)):
    if arr[i] == key:
        print("Found")
        break

    #binary search
    arr = [10,20,30,40,50]
key = 40

low = 0
high = len(arr)-1

while low <= high:
    mid = (low+high)//2

    if arr[mid] == key:
        print("Found")
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

 #bubble sort
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

arr = [64, 34, 25, 12, 22, 11, 90]

print("Sorted Array:", bubble_sort(arr))

print(arr)

#selection sort
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

arr = [64, 25, 12, 22, 11]
print("Sorted Array:", selection_sort(arr))

#merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return sorted(left + right)

arr = [38, 27, 43, 3, 9, 82, 10]
print("Sorted Array:", merge_sort(arr))