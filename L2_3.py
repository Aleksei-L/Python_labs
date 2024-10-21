import math


def cylinder():
	def circle(radius: float):
		return 2 * math.pi * radius

	user_input = int(input("Вы хотите:\n1) Вычислить полную площадь поверхности цилиндра\n2) Вычислить только площадь боковой поверхности цилиндра\nВаш выбор: "))
	if user_input != 1 and user_input != 2:
		raise ValueError("Выбран неверный пункт")
	radius = float(input("Введите радиус основания (разделитель - точка): "))
	height = float(input("Введите высоту цилиндра (разделитель - точка): "))
	print(2 * math.pi * radius * height + 2 * circle(radius)) if user_input == 1 else print(2 * math.pi * radius * height)


try:
	cylinder()
except ValueError:
	print("Ошибка")
