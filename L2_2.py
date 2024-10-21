def test():
	def positive():
		print("Положительное")

	def negative():
		print("Отрицательное")

	user_input = int(input("Введите число: "))
	if user_input > 0:
		positive()
	elif user_input < 0:
		negative()


test()
