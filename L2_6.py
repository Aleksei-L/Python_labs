def minus_list(first_list: list[int], second_list: list[int]):
	if len(first_list) != len(second_list):
		raise ValueError("Списки first_list и second_list должны быть одинаковой длины")
	arr = []
	for i in range(0, len(first_list)):
		arr.append(first_list[i] - second_list[i])
	return arr


print(minus_list([5, 4, 3], [2, 1, 3]))
print(minus_list([1, 2, 3], [4, 5, 6]))
try:
	minus_list([1, 2, 3], [4])
except ValueError:
	print("Ошибка")
