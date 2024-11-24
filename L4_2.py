class Book:
	def __init__(self, name, author, pages):
		self.__name = name
		self.__author = author
		self.__pages = pages

	@property
	def name(self):
		return self.__name

	@property
	def author(self):
		return self.__author

	@property
	def pages(self):
		return self.__pages

	def set_name(self, value):
		self.__name = value

	def print(self):
		print(f"Книга: name={self.name}, author={self.author}, pages={self.pages}")

	def get_price(self, cost_for_one_page):
		return self.pages * cost_for_one_page


class Publisher(Book):
	def __init__(self, name, author, pages, edition, language):
		super().__init__(name, author, pages)
		self.__edition = edition
		self.__language = language

	@property
	def edition(self):
		return self.__edition

	@property
	def language(self):
		return self.__language

	def print(self):
		print(
			f"Издательство: name={self.name}, author={self.author}, pages={self.pages}, edition={self.edition}, language={self.language}")

	def get_price(self, cost_for_one_page):
		return super().get_price(cost_for_one_page) * self.edition


b = Book("Имя", "Автор", 10)
b.print()
print(f"Цена: {b.get_price(2)}")
p = Publisher("Имя", "Автор", 10, 100, "Русский")
p.print()
print(f"Цена: {p.get_price(2)}")
