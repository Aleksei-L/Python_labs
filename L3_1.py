class Rectangle:
	def __init__(self, h, w):
		self.__height = h
		self.__width = w

	def __eq__(self, other):
		if isinstance(other, Rectangle):
			self_s = self.__width * self.__height
			other_s = other.width * other.height
			print("Площади этих прямоугольников равны") if self_s == other_s else print(
				"Площади этих прямоугольников не равны")

	@property
	def width(self):
		return self.__width

	@width.setter
	def width(self, w):
		if isinstance(w, int) and w > 0:
			self.__width = w

	@property
	def height(self):
		return self.__height

	def print(self):
		print(f"Ширина: {self.__width}, высота: {self.__height}")

	def print_p(self):
		print(f"Периметр: {2 * self.__height + 2 * self.__width}")

	def print_s(self):
		print(f"Площадь: {self.__width * self.__height}")


rec = Rectangle(3, 10)
rec.print()
rec.print_p()
rec.print_s()
rec.width = 5
rec.print()
rec.__eq__(Rectangle(3, 5))
rec.__eq__(Rectangle(3, 50))
