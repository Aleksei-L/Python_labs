string = "pythonist"
map = {}

for i in string:
	value = map.get(i)
	if value is None:
		map[i] = 1
	else:
		map[i] = map[i] + 1

print(f"Словарь: {map}")
