import random as rnd

arr = tuple(chr(rnd.randint(97, 101)) for i in range(1, 30))
print(f"Исходный кортеж: {arr}")

map = {}

for i in arr:
	value = map.get(i)
	if value is None:
		map[i] = 1
	else:
		map[i] = map[i] + 1

for i in map:
	print(f"Кол-во '{i}': {map[i]}")
