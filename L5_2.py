from abc import ABC, abstractmethod


class Home(ABC):
	@abstractmethod
	def __init__(self, width, height, length):
		self.width = width
		self.height = height
		self.length = length
		self.count_people = 0
		self.language = "None"

	@abstractmethod
	def print(self):
		print(f"Дом: width={self.width}, height={self.height}, length={self.length}")

	@abstractmethod
	def set_people(self, value):
		self.count_people = value

	@abstractmethod
	def set_language(self, value):
		self.language = value


class City(Home):
	def __init__(self, width, height, length, count_people, language, count_home):
		super().__init__(width, height, length)
		super().set_people(count_people)
		super().set_language(language)
		self.count_home = count_home

	def print(self):
		print(
			f"Город: width={self.width}, height={self.height}, length={self.length}, count_people={self.count_people}, language={self.language}, count_home={self.count_home}")

	def set_people(self, value):
		super().set_people(value)

	def set_language(self, value):
		super().set_language(value)


class Country(City):
	def __init__(self, width, height, length, count_people, language, count_home, count_city):
		super().__init__(width, height, length, count_people, language, count_home)
		self.count_city = count_city

	def print(self):
		print(
			f"Страна: width={self.width}, height={self.height}, length={self.length}, count_people={self.count_people}, language={self.language}, count_home={self.count_home}, count_city={self.count_city}")

	def set_people(self, value):
		super().set_people(value)

	def set_language(self, value):
		super().set_language(value)

	def count_people_fun(self):
		return self.count_city * self.count_home * self.count_people


c = City(1, 1, 1, 10, "Русский", 5)
c.print()
co = Country(2, 2, 2, 20, "Русский", 5, 3)
co.print()
print(f"Кол-во жителей страны: {co.count_people_fun()}")
