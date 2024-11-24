import random


class List:
	def __init__(self, size):
		self.__size = size
		self.__arr = [0] * self.__size

	@property
	def arr(self):
		return self.__arr

	@property
	def size(self):
		return self.__size

	def input_data(self, *args):
		for i in range(0, self.__size):
			self.__arr[i] = args[i]

	def input_data_random(self):
		for i in range(0, self.__size):
			self.__arr[i] = random.randint(0, 10)

	def print(self):
		print("Список: ", end='')
		for i in self.__arr:
			print(i, end=' ')
		print()

	def find_value(self, value):
		res = []
		for i in range(0, self.__size):
			if self.__arr[i] == value:
				res.append(i)
		return res

	def del_value(self, value):
		index_for_del = []
		for i in range(0, self.__size):
			if self.__arr[i] == value:
				index_for_del.append(i)

		self.__size -= len(index_for_del)
		for i in index_for_del:
			self.__arr.pop(i)

	def find_max(self):
		return max(self.__arr)

	def __add__(self, other):
		if isinstance(other, List) and self.__size == other.__size:
			for i in range(0, self.__size):
				self.__arr[i] += other.__arr[i]
		return self.__arr


l = List(6)
l.input_data(1, 5, 6, 7, 8, 7)
l.print()
l.del_value(1)
l.print()
print(f"7 найдены под индексами: {l.find_value(7)}")
print(f"Максимальный элемент в списке: {l.find_max()}")
l2 = List(5)
l2.input_data_random()
l2.print()
l + l2
l.print()
