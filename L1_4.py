import random as rnd

arr = [rnd.randint(1, 10) for i in range(1, 10)]
print(f"Исходный список: {arr}")

minim = 11
minim_index = -1
maxim = 0
maxim_index = -1

for i in range(0, len(arr)):
	if arr[i] > maxim:
		maxim = arr[i]
		maxim_index = i
	elif arr[i] < minim:
		minim = arr[i]
		minim_index = i

temp = arr[minim_index]
arr[minim_index] = arr[maxim_index]
arr[maxim_index] = temp

print(f"Массив с обменом: {arr}")
