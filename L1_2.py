import random as rnd

arr = [rnd.randint(1, 5) for i in range(1, 10 + 1)]
print(f"Исходный список: {arr}")

zipped_list = []

for i in arr:
	if zipped_list.count(i) == 0:
		zipped_list.append(i)

print(f"Сжатый список: {zipped_list}")
