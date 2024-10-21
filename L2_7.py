def make_matrix(size: tuple, value=0):
	matrix = []
	if len(size) != 1 and len(size) != 2:
		raise ValueError("Параметр size функции make_matrix принимает только кортеж из 1 или 2 элементов")
	for i in range(0, size[0]):
		matrix.append([])
		for j in range(0, size[0] if len(size) == 1 else size[1]):
			matrix[i].append(value)
	return matrix


print(make_matrix((2, 3), 10))
print(make_matrix((4, 2)))
print(make_matrix((3,), 15))
try:
	print(make_matrix(tuple([1, 1, 1]), 15))
except ValueError:
	print("Ошибка")
