class Student:
	def __init__(self, name="Ivan", age=18, group_number="10A"):
		self.__name = name
		self.__age = age
		self.__group_number = group_number

	@property
	def name(self):
		return self.__name

	@property
	def age(self):
		return self.__age

	@property
	def group_number(self):
		return self.__group_number

	@name.setter
	def name(self, value):
		self.__name = value

	@age.setter
	def age(self, value):
		self.__age = value

	@group_number.setter
	def group_number(self, value):
		self.__group_number = value

	def print(self):
		print(f"Студент: имя={self.name}, возраст={self.age}, группа={self.group_number}")


s_1 = Student()
s_1.name = "Student 1"
s_1.age = 19
s_1.group_number = "AAA"
s_1.print()
s_2 = Student()
s_2.name = "Student 2"
s_2.age = 20
s_2.group_number = "BBB"
s_2.print()
s_3 = Student()
s_3.name = "Student 3"
s_3.age = 21
s_3.group_number = "CCC"
s_3.print()
