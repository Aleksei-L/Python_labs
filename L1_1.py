import random as rnd

arr = [rnd.randint(1, 10) for i in range(0, 10)]
arr.sort()

print(f"Массив: {arr}")

map = {}

for i in arr:
	value = map.get(i)
	if value is None:
		map[i] = 1
	else:
		map[i] = map[i] + 1

print(f"Кол-во повторений: {map}")
