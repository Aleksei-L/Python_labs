class TArray:
	def __init__(self, size=1, value=0):
		self.__size = size
		self.__arr = [value] * size

	def __copy__(self):
		new_arr = TArray(self.__size)
		for i in range(0, len(new_arr.__arr)):
			new_arr.__arr[i] = self.__arr[i]
		return new_arr

	def input_data(self):
		self.__arr = []
		print(f"Введите {self.__size} элементов массива:")
		for i in range(self.__size):
			self.__arr.append(int(input()))

	def print(self):
		print(f"Массив: {self.__arr}")

	def max_element(self):
		return max(self.__arr)

	def min_element(self):
		return min(self.__arr)

	def sort_array(self):
		self.__arr.sort()

	def sum_elements(self):
		return sum(self.__arr)

	def __add__(self, element):
		self.__arr.append(element)
		self.__size += 1
		return self

	def __mul__(self, number):
		self.__arr = [x * number for x in self.__arr]
		return self


arr = TArray(5, 1)
new_arr = arr.__copy__()
arr.print()
arr.input_data()
arr.print()
print(f"Максимальный элемент: {arr.max_element()}")
print(f"Минимальный элемент: {arr.min_element()}")
print(f"Сумма элементов: {arr.sum_elements()}")
arr.sort_array()
new_arr.print()
arr.print()
arr += 10
arr.print()
arr = arr * 2
arr.print()
