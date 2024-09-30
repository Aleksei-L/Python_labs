import random as rnd

arr_1 = [rnd.randint(1, 100) for i in range(1, 10_000)]
arr_2 = [rnd.randint(1, 100) for i in range(1, 10_000)]

set_1 = set(arr_1)
set_2 = set(arr_2)

print(f"Общие элементы: {set_1.intersection(set_2)}")
