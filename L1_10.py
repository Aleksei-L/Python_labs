import random as rnd

arr = [rnd.randint(1, 100) for i in range(1, 100_000)]

print(f"Кол-во уникальных элементов в списке: {len(set(arr))}")
