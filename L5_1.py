from abc import ABC, abstractmethod
from math import pi


class Figure(ABC):
	@abstractmethod
	def print(self):
		pass

	@abstractmethod
	def set_color(self, value):
		pass


class Point(Figure):
	def __init__(self, x, y):
		self.__x = x
		self.__y = y
		self.__color = "None"

	@property
	def x(self):
		return self.__x

	@property
	def y(self):
		return self.__y

	@property
	def color(self):
		return self.__color

	def print(self):
		print(f"Точка: x={self.x}, y={self.y}, color={self.color}")

	def set_color(self, value):
		self.__color = value


class Circle(Point):
	def __init__(self, x_center, y_center, radius):
		super().__init__(x_center, y_center)
		self.__radius = radius

	@property
	def radius(self):
		return self.__radius

	def print(self):
		print(f"Круг: x_center={self.x}, y_center={self.y}, radius={self.radius}, color={self.color}")

	def set_radius(self, value):
		self.__radius = value

	def square(self):
		return pi * self.radius ** 2


class Sphere(Circle):
	def __init__(self, x_center, y_center, z_center, radius):
		super().__init__(x_center, y_center, radius)
		self.__z_center = z_center

	@property
	def z_center(self):
		return self.__z_center

	def print(self):
		print(
			f"Сфера: x_center={self.x}, y_center={self.y}, z_center={self.z_center}, radius={self.radius}, color={self.color}")

	def square(self):
		return 4 * super().square()

	def set_radius(self, value):
		super().set_radius(value)
