import random as rnd

keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
values = [chr(rnd.randint(97, 101)) for i in range(0, 10)]

print(f"Ключи: {keys}")
print(f"Значения: {values}")

map = dict(zip(keys, values))

print(f"Словарь: {map}")
