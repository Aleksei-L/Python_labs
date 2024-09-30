import random as rnd

keys = ["Key " + str(i) for i in range(1, 11)]
values = [rnd.randint(1, 5) for i in range(0, 10)]
map = dict(zip(keys, values))

print(f"Словарь: {map}")

number = 1
for i in map.values():
	number *= i

print(f"Произведение значений: {number}")
