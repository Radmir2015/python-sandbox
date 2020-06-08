import random

lst = random.sample(range(1, 10), 9)

counter = 0

def sort(arr, i=0, j=0, length=0):
	if length == 0 and arr:
		length = len(arr)

	if i >= length - 1:
		if j < length - 2:
			sort(arr, 0, j + 1, length)
		return

	if arr[i] > arr[i + 1]:
		arr[i], arr[i + 1] = arr[i + 1], arr[i]

	global counter
	counter += 1

	sort(arr, i + 1, j, length)

sort(lst)

print(lst, counter)