import random as rnd

arr = [rnd.randint(19, 21) for i in range(1, 10)]
print(f"Исходный список: {arr}")

for i in range(0, len(arr)):
	if arr[i] == 20:
		arr[i] = 200
		break

print(f"Новый список: {arr}")
