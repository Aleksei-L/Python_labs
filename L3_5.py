class Bus:
	def __init__(self, speed, capacity, max_speed):
		self.__speed = speed
		self.__capacity = capacity
		self.__max_speed = max_speed
		self.__passengers = []
		self.__has_empty_seats = True
		self.__seats = {i: None for i in range(0, capacity)}

	def board_passengers(self, *new_passengers):
		for i in new_passengers:
			if not self.__has_empty_seats:
				print(f"Нет свободных мест для пассажира {i}")
				continue
			for seat, passenger in self.__seats.items():
				if passenger is None:
					self.__seats[seat] = i
					self.__passengers.append(i)
					print(f"Пассажир {i} занял место {seat}")
					break

	def remove_passengers(self, *names):
		for i in names:
			if i not in self.__passengers:
				print(f"Пассажир {i} не найден в автобусе")
				continue
			self.__passengers.remove(i)
			for seat, passenger in self.__seats.items():
				if passenger == i:
					self.__seats[seat] = None
					print(f"Пассажир {i} покинул место {seat}")
					break

	def plus_speed(self, value):
		if self.__speed + value > self.__max_speed:
			self.__speed = self.__max_speed
			print(f"Скорость увеличена до максимальной {self.__max_speed}")
		else:
			self.__speed += value
			print(f"Скорость увеличена до {self.__speed}")

	def minus_speed(self, value):
		if self.__speed - value < 0:
			self.__speed = 0
		else:
			self.__speed -= value
		print(f"Скорость уменьшена до {self.__speed}")

	def __contains__(self, name):
		return name in self.__passengers

	def __iadd__(self, names):
		if isinstance(names, str):
			self.board_passengers(names)
		elif isinstance(names, (list, tuple)):
			self.board_passengers(*names)
		return self

	def __isub__(self, names):
		if isinstance(names, str):
			self.remove_passengers(names)
		elif isinstance(names, (list, tuple)):
			self.remove_passengers(*names)
		return self

	def print(self):
		print(f"Автобус: скорость={self.__speed}, вместимость={self.__capacity}, максимальная скорость={self.__max_speed}, пассажиры={self.__passengers}, есть свободные места={self.__has_empty_seats}, места={self.__seats}")


b = Bus(15, 5, 40)
b.board_passengers("Иван", "Анна", "Олег")
b.print()
print("Иван" in b)
b.plus_speed(100)
b.minus_speed(10)
b += "Мария"
b += ["Алексей", "Дмитрий"]
b.print()
b -= "Анна"
b -= ["Иван", "Мария"]
b.print()
