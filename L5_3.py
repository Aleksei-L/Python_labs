class Games:
	Year = None

	def __init__(self, year):
		Games.Year = year
		self.name = "None"

	def get_name(self):
		return self.name


class PCGames(Games):
	def __init__(self, year, name, platform):
		super().__init__(year)
		self.name = name
		self.platform = platform

	def get_name(self):
		return f"PC Game: name={self.name}, platform={self.platform}"


class PS4Games(Games):
	def __init__(self, year, name, exclusive):
		super().__init__(year)
		self.name = name
		self.exclusive = exclusive

	def get_name(self):
		return f"PS4 Game: name={self.name}, exclusive={"yes" if self.exclusive else "no"}"


class XboxGames(Games):
	def __init__(self, year, name, multiplayer):
		super().__init__(year)
		self.name = name
		self.multiplayer = multiplayer

	def get_name(self):
		return f"Xbox Game: name={self.name}, multiplayer={"yes" if self.multiplayer else "no"}"


class MobileGames(Games):
	def __init__(self, year, name, store):
		super().__init__(year)
		self.name = name
		self.store = store

	def get_name(self):
		return f"Mobile Game: name={self.name}, store={self.store}"


pc_game = PCGames(2024, "Name 1", "PC")
ps4_game = PS4Games(2023, "Name 2", True)
xbox_game = XboxGames(2022, "Name 3", True)
mobile_game = MobileGames(2021, "Name 4", "Store")

print(pc_game.get_name())
print(ps4_game.get_name())
print(xbox_game.get_name())
print(mobile_game.get_name())

print(f"Year: {Games.Year}")
