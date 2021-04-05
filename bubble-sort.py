def bubble_sort(arr):
  n = len(arr)
  for i in range(n-1):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]

nums = [5, 3, 8, 6]
bubble_sort(nums)
print(f"nums should be [3, 5, 6, 8] and is, in fact: {nums}")
